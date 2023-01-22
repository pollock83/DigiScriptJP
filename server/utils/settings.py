from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING

from tornado.locks import Lock

from utils.logger import get_logger
from utils.file_watcher import IOLoopFileWatcher

if TYPE_CHECKING:
    from server.server.app_server import DigiScriptServer


class SettingsObject:
    def __init__(self, key, val_type, default, can_edit=True, callback_fn=None):
        if val_type not in [str, bool, int]:
            raise RuntimeError(f'Invalid type {val_type} for {key}. Allowed options are: '
                               f'[str, int, bool]')

        self.key = key
        self.val_type = val_type
        self.value = None
        self.default = default
        self.can_edit = can_edit
        self._callback_fn = callback_fn
        self._loaded = False

    def set_to_default(self):
        self.value = self.default
        self._loaded = True

    def set_value(self, value, spawn_callbacks=True):
        if not isinstance(value, self.val_type):
            raise RuntimeError(f'Value for {self.key} of {value} is not of assigned '
                               f'type {self.val_type}')

        changed = False
        if value != self.value:
            changed = True
            self.value = value
            if self._callback_fn and spawn_callbacks:
                self._callback_fn()

        self._loaded = True
        return changed

    def get_value(self):
        return self.value

    def is_loaded(self):
        return self._loaded

    def as_json(self):
        return {
            'type': self.val_type.__name__,
            'value': self.value,
            'default': self.default,
            'can_edit': self.can_edit
        }


class Settings:
    def __init__(self, application: DigiScriptServer, settings_path=None):
        self._application = application
        self.lock = Lock()
        self._base_path = os.path.join(os.path.dirname(__file__), '..', 'conf')
        if settings_path:
            self.settings_path = settings_path
        else:
            self.settings_path = os.path.join(self._base_path, 'digiscript.json')
            get_logger().info(
                f'No settings path provided, using {self.settings_path}')

        self.settings = {}

        self.define('debug_mode', bool, False, True)
        self.define('current_show', int, False, False)
        self.define('log_path', str, os.path.join(self._base_path, 'digiscript.log'), True,
                    self._application.regen_logging)
        self.define('max_log_mb', int, 100, True, self._application.regen_logging)
        self.define('log_backups', int, 5, True, self._application.regen_logging)
        self.define('db_log_enabled', bool, False, True, self._application.regen_logging)
        self.define('db_log_path', str, os.path.join(self._base_path, 'digiscript_db.log'), True,
                    self._application.regen_logging)
        self.define('db_max_log_mb', int, 100, True, self._application.regen_logging)
        self.define('db_log_backups', int, 5, True, self._application.regen_logging)

        self._load(spawn_callbacks=False)

        self._file_watcher = IOLoopFileWatcher(self.settings_path, self.auto_reload_changes, 100)
        self._file_watcher.add_error_callback(self.file_deleted)
        self._file_watcher.watch()

    def define(self, key, val_type, default, can_edit, callback_fn=None):
        self.settings[key] = SettingsObject(key, val_type, default, can_edit, callback_fn)

    def file_deleted(self):
        get_logger().info('Settings file deleted; recreating from in memory settings')
        self._save()

    def auto_reload_changes(self):
        get_logger().info('Settings file changed; auto reloading')
        self._load(spawn_callbacks=True)

        settings_json = {}
        for key, value in self.settings.items():
            settings_json[key] = value.get_value()

        for client in self._application.clients:
            client.write_message({
                'OP': 'SETTINGS_CHANGED',
                'DATA': settings_json,
                'ACTION': 'WS_SETTINGS_CHANGED'
            })

    def _load(self, spawn_callbacks=False):
        if os.path.exists(self.settings_path):
            # Read in the settings
            with open(self.settings_path, 'r', encoding='UTF-8') as file_pointer:
                settings = json.load(file_pointer)
                for key, value in settings.items():
                    if key not in self.settings:
                        get_logger().warning(f'Setting {key} found in settings file is not '
                                             f'defined, ignoring!')
                    else:
                        self.settings[key].set_value(value, spawn_callbacks)

            # Set any missing settings to their defaults, and save if needed
            needs_saving = False
            for key, value in self.settings.items():
                if not value.is_loaded():
                    value.set_from_default()
                    needs_saving = True
            if needs_saving:
                with open(self.settings_path, 'w', encoding='UTF-8') as file_pointer:
                    json.dump(self._json(), file_pointer, indent=4)
                get_logger().info(f'Saved settings to {self.settings_path}')

            get_logger().info(f'Loaded settings from {self.settings_path}')
        else:
            # Set everything to its default value
            for key, value in self.settings.items():
                value.set_to_default()

            with open(self.settings_path, 'w', encoding='UTF-8') as file_pointer:
                json.dump(self._json(), file_pointer, indent=4)

            get_logger().info(f'Saved settings to {self.settings_path}')

    def _save(self):
        self._file_watcher.pause()
        with open(self.settings_path, 'w', encoding='UTF-8') as file_pointer:
            json.dump(self._json(), file_pointer, indent=4)
            file_pointer.flush()
            os.fsync(file_pointer.fileno())
            self._file_watcher.update_m_time()
        self._file_watcher.resume()
        get_logger().info(f'Saved settings to {self.settings_path}')

    async def get(self, key):
        async with self.lock:
            return self.settings.get(key).get_value()

    async def set(self, key, item):
        changed = False
        async with self.lock:
            if key not in self.settings:
                get_logger().warning(f'Setting {key} found in settings file is not '
                                     f'defined, ignoring!')
            else:
                changed = self.settings[key].set_value(item)

        if changed:
            self._save()
            settings = await self.as_json()
            await self._application.ws_send_to_all('SETTINGS_CHANGED', 'WS_SETTINGS_CHANGED',
                                                   settings)

    def _json(self):
        settings_json = {}
        for key, value in self.settings.items():
            settings_json[key] = value.get_value()
        return settings_json

    async def as_json(self):
        async with self.lock:
            settings_json = {}
            for key, value in self.settings.items():
                settings_json[key] = value.get_value()
            return json.loads(json.dumps(settings_json))

    async def raw_json(self):
        async with self.lock:
            settings_json = {}
            for key, value in self.settings.items():
                settings_json[key] = value.as_json()
            return json.loads(json.dumps(settings_json))
