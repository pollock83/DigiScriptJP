# Pylint-Ignore

**WARNING: This file is programmatically generated.**

This file is parsed by [`pylint-ignore`](https://pypi.org/project/pylint-ignore/)
to determine which
[Pylint messages](https://pylint.pycqa.org/en/stable/technical_reference/features.html)
should be ignored.

- Do not edit this file manually.
- To update, use `pylint-ignore --update-ignorefile`

The recommended approach to using `pylint-ignore` is:

1. If a message refers to a valid issue, update your code rather than
   ignoring the message.
2. If a message should *always* be ignored (globally), then to do so
   via the usual `pylintrc` or `setup.cfg` files rather than this
   `pylint-ignore.md` file.
3. If a message is a false positive, add a comment of this form to your code:
   `# pylint:disable=<symbol> ; explain why this is a false positive`


# Overview

 - [E0401: import-error (1x)](#e0401-import-error)
 - [E0611: no-name-in-module (1x)](#e0611-no-name-in-module)
 - [E1101: no-member (3x)](#e1101-no-member)
 - [W0212: protected-access (1x)](#w0212-protected-access)
 - [W0511: fixme (1x)](#w0511-fixme)
 - [W0611: unused-import (1x)](#w0611-unused-import)
 - [W0613: unused-argument (1x)](#w0613-unused-argument)
 - [W0703: broad-except (1x)](#w0703-broad-except)
 - [W1203: logging-fstring-interpolation (11x)](#w1203-logging-fstring-interpolation)
 - [W1514: unspecified-encoding (5x)](#w1514-unspecified-encoding)
 - [C0103: invalid-name (7x)](#c0103-invalid-name)
 - [C0114: missing-module-docstring (13x)](#c0114-missing-module-docstring)
 - [C0115: missing-class-docstring (18x)](#c0115-missing-class-docstring)
 - [C0116: missing-function-docstring (19x)](#c0116-missing-function-docstring)
 - [C0209: consider-using-f-string (4x)](#c0209-consider-using-f-string)
 - [C0412: ungrouped-imports (4x)](#c0412-ungrouped-imports)
 - [R0205: useless-object-inheritance (2x)](#r0205-useless-object-inheritance)
 - [R0903: too-few-public-methods (3x)](#r0903-too-few-public-methods)


# E0401: import-error

## File main.py - Line 8 - E0401 (import-error)

- `message: Unable to import 'server.app_server'`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   6: 
   7: from utils.logger import get_logger, add_logging_level
>  8: from server.app_server import DigiScriptServer
   9: 
  10: add_logging_level('TRACE', logging.DEBUG - 5)
```


# E0611: no-name-in-module

## File main.py - Line 8 - E0611 (no-name-in-module)

- `message: No name 'app_server' in module 'server'`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   6: 
   7: from utils.logger import get_logger, add_logging_level
>  8: from server.app_server import DigiScriptServer
   9: 
  10: add_logging_level('TRACE', logging.DEBUG - 5)
```


# E1101: no-member

## File server/app_server.py - Line 17 - E1101 (no-member)

- `message: Class 'EnvParser' has no 'instance' member`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  15: 
  16:     def __init__(self, debug=False, settings_path=None):
> 17:         env_parser: EnvParser = EnvParser.instance()
  18: 
  19:         self.digi_settings = Settings(settings_path)
```


## File utils/route.py - Line 36 - E1101 (no-member)

- `message: Module 'urllib' has no 'quote' member`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  34:     @staticmethod
  35:     def _url_escape(v):
> 36:         return urllib.quote(tornado.escape.utf8(v), '')
  37: 
  38:     @classmethod
```


## File utils/route.py - Line 42 - E1101 (no-member)

- `message: Instance of 'dict' has no 'iteritems' member`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  39:     def make(cls, _name, **kwargs):
  ...
  40:         if _name not in cls._formats:
  41:             raise KeyError('No route by the name of `{}`'.format(_name))
> 42:         kwargs = {k: cls._url_escape(v) for k, v in kwargs.iteritems()}
  43:         return cls._formats[_name] % kwargs
  44:
```


# W0212: protected-access

## File utils/logger.py - Line 24 - W0212 (protected-access)

- `message: Access to a protected member _log of a client class`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  22:     def log_for_level(self, message, *args, **kwargs):
  23:         if self.isEnabledFor(level_num):
> 24:             self._log(level_num, message, args, **kwargs)
  25: 
  26:     def log_to_root(message, *args, **kwargs):
```


# W0511: fixme

## File controllers/ws_controller.py - Line 48 - W0511 (fixme)

- `message: TODO: This assumes only one session from a single client IP, which`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  44:     def on_close(self) -> None:
  ...
  46:             self.application.clients.remove(self)
  47: 
> 48:         # TODO: This assumes only one session from a single client IP, which
  49:         # might not be true
  50:         with self.make_session() as session:
```


# W0611: unused-import

## File utils/route.py - Line 1 - W0611 (unused-import)

- `message: Unused ABC imported from abc`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
> 1: from abc import ABC
  2: from enum import Enum
  3: import urllib
```


# W0613: unused-argument

## File controllers/controllers.py - Line 15 - W0613 (unused-argument)

- `message: Unused argument 'path'`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  13: 
  14: class RootController(BaseController):
> 15:     def get(self, path):
  16:         file_path = os.path.join(
  17:             os.path.abspath(
```


# W0703: broad-except

## File controllers/api/shows.py - Line 52 - W0703 (broad-except)

- `message: Catching too general exception BaseException`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  13:     def post(self):
  ...
  50:             if not end_date:
  51:                 raise Exception
> 52:         except BaseException:
  53:             self.set_status(400)
  54:             self.write({'message': 'Unable to parse end date value'})
```


# W1203: logging-fstring-interpolation

## File utils/settings.py - Line 16 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   9:     def __init__(self, settings_path=None):
  ...
  14:             self.settings_path = os.path.join(
  15:                 os.path.dirname(__file__), "../digiscript.json")
> 16:             get_logger().info(
  17:                 f'No settings path provided, using {self.settings_path}')
  18:         self.settings = {}
```


## File controllers/api/shows.py - Line 18 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  13:     def post(self):
  ...
  16:         """
  17:         data = escape.json_decode(self.request.body)
> 18:         get_logger().debug(f'New show data posted: {data}')
  19: 
  20:         # Name
```


## File controllers/api/settings.py - Line 21 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  11: class SettingsController(BaseAPIController):
  ...
  19: 
  20:         data = escape.json_decode(self.request.body)
> 21:         get_logger().debug(f'New settings data patched: {data}')
  22: 
  23:         for k, v in data.items():
```


## File server/app_server.py - Line 22 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  16:     def __init__(self, debug=False, settings_path=None):
  ...
  20:         self.clients = []
  21: 
> 22:         get_logger().info(f'Using {env_parser.db_path} as DB path')
  23:         self.db = db
  24:         self.db.configure(url=env_parser.db_path)
```


## File utils/settings.py - Line 25 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  ...
  23:             with open(self.settings_path, 'r') as fp:
  24:                 self.settings = json.load(fp)
> 25:             get_logger().info(f'Loaded settings from {self.settings_path}')
  26:         else:
  27:             self._create_defaults()
```


## File main.py - Line 27 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  22: def main():
  ...
  25:                            settings_path=options.settings_path)
  26:     app.listen(options.port)
> 27:     get_logger().info(f'Listening on port: {options.port}')
  28:     if options.debug:
  29:         get_logger().warning('Running in debug mode')
```


## File utils/settings.py - Line 30 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  ...
  28:             with open(self.settings_path, 'w') as fp:
  29:                 json.dump(self.settings, fp)
> 30:             get_logger().info(f'Saved settings to {self.settings_path}')
  31: 
  32:     def _save(self):
```


## File utils/settings.py - Line 35 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  32:     def _save(self):
  ...
  33:         with open(self.settings_path, 'w') as fp:
  34:             json.dump(self.settings, fp)
> 35:         get_logger().info(f'Saved settings to {self.settings_path}')
  36: 
  37:     def _create_defaults(self):
```


## File controllers/ws_controller.py - Line 42 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  36:     def open(self, *args: str, **kwargs: str) -> Optional[Awaitable[None]]:
  ...
  40:         # might not be true
  41:         self.update_session()
> 42:         get_logger().info(f'WebSocket opened from: {self.request.remote_ip}')
  43: 
  44:     def on_close(self) -> None:
```


## File controllers/ws_controller.py - Line 56 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  44:     def on_close(self) -> None:
  ...
  54:                 session.commit()
  55: 
> 56:         get_logger().info(f'WebSocket closed from: {self.request.remote_ip}')
  57: 
  58:     def on_message(self, message: Union[str, bytes]
```


## File controllers/ws_controller.py - Line 60 - W1203 (logging-fstring-interpolation)

- `message: Use lazy % formatting in logging functions`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  58:     def on_message(self, message: Union[str, bytes]
  59:                    ) -> Optional[Awaitable[None]]:
> 60:         get_logger().debug(
  61:             f'WebSocket received data from {self.request.remote_ip}: {message}')
  62:
```


# W1514: unspecified-encoding

## File controllers/controllers.py - Line 21 - W1514 (unspecified-encoding)

- `message: Using open without explicitly specifying an encoding`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  15:     def get(self, path):
  ...
  19:             "..",
  20:             "public")
> 21:         with open(os.path.join(file_path, "index.html"), 'r') as file:
  22:             self.write(file.read())
  23:
```


## File utils/settings.py - Line 23 - W1514 (unspecified-encoding)

- `message: Using open without explicitly specifying an encoding`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  22:         if os.path.exists(self.settings_path):
> 23:             with open(self.settings_path, 'r') as fp:
  24:                 self.settings = json.load(fp)
  25:             get_logger().info(f'Loaded settings from {self.settings_path}')
```


## File utils/settings.py - Line 28 - W1514 (unspecified-encoding)

- `message: Using open without explicitly specifying an encoding`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  ...
  26:         else:
  27:             self._create_defaults()
> 28:             with open(self.settings_path, 'w') as fp:
  29:                 json.dump(self.settings, fp)
  30:             get_logger().info(f'Saved settings to {self.settings_path}')
```


## File utils/settings.py - Line 33 - W1514 (unspecified-encoding)

- `message: Using open without explicitly specifying an encoding`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  31: 
  32:     def _save(self):
> 33:         with open(self.settings_path, 'w') as fp:
  34:             json.dump(self.settings, fp)
  35:         get_logger().info(f'Saved settings to {self.settings_path}')
```


## File controllers/controllers.py - Line 34 - W1514 (unspecified-encoding)

- `message: Using open without explicitly specifying an encoding`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  26:     def get(self):
  ...
  32:                 os.path.sep))
  33:         try:
> 34:             with open(full_path, 'r') as file:
  35:                 self.write(file.read())
  36:         except UnicodeDecodeError:
```


# C0103: invalid-name

## File server/app_server.py - Line 23 - C0103 (invalid-name)

- `message: Attribute name "db" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  16:     def __init__(self, debug=False, settings_path=None):
  ...
  21: 
  22:         get_logger().info(f'Using {env_parser.db_path} as DB path')
> 23:         self.db = db
  24:         self.db.configure(url=env_parser.db_path)
  25:         self.db.create_all()
```


## File utils/settings.py - Line 23 - C0103 (invalid-name)

- `message: Variable name "fp" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  22:         if os.path.exists(self.settings_path):
> 23:             with open(self.settings_path, 'r') as fp:
  24:                 self.settings = json.load(fp)
  25:             get_logger().info(f'Loaded settings from {self.settings_path}')
```


## File controllers/api/settings.py - Line 23 - C0103 (invalid-name)

- `message: Variable name "v" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  11: class SettingsController(BaseAPIController):
  ...
  21:         get_logger().debug(f'New settings data patched: {data}')
  22: 
> 23:         for k, v in data.items():
  24:             await settings.set(k, v)
  25:
```


## File utils/settings.py - Line 28 - C0103 (invalid-name)

- `message: Variable name "fp" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  21:     def _load(self):
  ...
  26:         else:
  27:             self._create_defaults()
> 28:             with open(self.settings_path, 'w') as fp:
  29:                 json.dump(self.settings, fp)
  30:             get_logger().info(f'Saved settings to {self.settings_path}')
```


## File utils/settings.py - Line 33 - C0103 (invalid-name)

- `message: Variable name "fp" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  31: 
  32:     def _save(self):
> 33:         with open(self.settings_path, 'w') as fp:
  34:             json.dump(self.settings, fp)
  35:         get_logger().info(f'Saved settings to {self.settings_path}')
```


## File utils/route.py - Line 35 - C0103 (invalid-name)

- `message: Argument name "v" doesn't conform to snake_case naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: class Route(object):
  ...
  33: 
  34:     @staticmethod
> 35:     def _url_escape(v):
  36:         return urllib.quote(tornado.escape.utf8(v), '')
  37:
```


## File utils/route.py - Line 47 - C0103 (invalid-name)

- `message: Class constant name "v1" doesn't conform to UPPER_CASE naming style`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  45: 
  46: class ApiVersion(Enum):
> 47:     v1 = 1
  48: 
  49:
```


# C0114: missing-module-docstring

## File controllers/api/settings.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File controllers/api/shows.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File controllers/base_controller.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File controllers/controllers.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File controllers/ws_controller.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File main.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File models/models.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File server/app_server.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File utils/env_parser.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File utils/logger.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File utils/route.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File utils/settings.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


## File utils/singleton.py - C0114 (missing-module-docstring)

- `message: Missing module docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`


# C0115: missing-class-docstring

## File controllers/base_controller.py - Line 7 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   5: 
   6: 
>  7: class BaseController(SessionMixin, RequestHandler):
   8:     def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
   9:         raise RuntimeError(
```


## File utils/env_parser.py - Line 7 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   5: 
   6: @Singleton
>  7: class EnvParser(object):
   8: 
   9:     def __init__(self):
```


## File utils/settings.py - Line 8 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   6: 
   7: 
>  8: class Settings:
   9:     def __init__(self, settings_path=None):
  10:         self.lock = Lock()
```


## File controllers/api/settings.py - Line 11 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   9: 
  10: @ApiRoute('settings', ApiVersion.v1)
> 11: class SettingsController(BaseAPIController):
  12:     async def get(self):
  13:         settings: Settings = self.application.digi_settings
```


## File controllers/api/shows.py - Line 12 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  10: 
  11: @ApiRoute('show', ApiVersion.v1)
> 12: class ShowController(BaseAPIController):
  13:     def post(self):
  14:         """
```


## File controllers/ws_controller.py - Line 12 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  10: 
  11: @ApiRoute('ws', ApiVersion.v1)
> 12: class WebSocketController(SessionMixin, WebSocketHandler):
  13: 
  14:     def update_session(self):
```


## File controllers/base_controller.py - Line 13 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  11: 
  12: 
> 13: class BaseAPIController(BaseController):
  14: 
  15:     def _unimplemented_method(self, *args: str, **kwargs: str) -> None:
```


## File controllers/controllers.py - Line 14 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: 
  13: 
> 14: class RootController(BaseController):
  15:     def get(self, path):
  16:         file_path = os.path.join(
```


## File server/app_server.py - Line 14 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: 
  13: 
> 14: class DigiScriptServer(Application):
  15: 
  16:     def __init__(self, debug=False, settings_path=None):
```


## File models/models.py - Line 24 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  22: 
  23: 
> 24: class Session(db.Model):
  25:     __tablename__ = 'sessions'
  26:
```


## File controllers/controllers.py - Line 25 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  23: 
  24: 
> 25: class StaticController(BaseController):
  26:     def get(self):
  27:         self.set_header('Content-Type', '')
```


## File models/models.py - Line 32 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  30: 
  31: 
> 32: class Show(db.Model):
  33:     __tablename__ = 'shows'
  34:
```


## File controllers/controllers.py - Line 41 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  39: 
  40: 
> 41: class ApiFallback(BaseAPIController):
  42:     def get(self):
  43:         self.set_status(404)
```


## File utils/route.py - Line 46 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  44: 
  45: 
> 46: class ApiVersion(Enum):
  47:     v1 = 1
  48:
```


## File utils/route.py - Line 50 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  48: 
  49: 
> 50: class ApiRoute(Route):
  51:     def __init__(self, route: str, api_version: ApiVersion, name: str = None):
  52:         route = f'/api/v{api_version.value}/{route}'
```


## File controllers/controllers.py - Line 60 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  58: 
  59: @Route('/debug')
> 60: class DebugController(BaseController):
  61:     def get(self):
  62:         self.set_status(200)
```


## File controllers/controllers.py - Line 68 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  66: 
  67: @ApiRoute('debug', ApiVersion.v1)
> 68: class ApiDebugController(BaseAPIController):
  69:     def get(self):
  70:         self.set_status(200)
```


## File controllers/api/shows.py - Line 86 - C0115 (missing-class-docstring)

- `message: Missing class docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  84: 
  85: @ApiRoute('shows', ApiVersion.v1)
> 86: class ShowsController(BaseAPIController):
  87: 
  88:     def get(self):
```


# C0116: missing-function-docstring

## File utils/logger.py - Line 4 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  2: 
  3: 
> 4: def get_logger():
  5:     return logging.getLogger('DigiScript')
  6:
```


## File utils/logger.py - Line 8 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   6: 
   7: 
>  8: def add_logging_level(level_name, level_num, method_name=None):
   9:     if not method_name:
  10:         method_name = level_name.lower()
```


## File models/models.py - Line 9 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   7: 
   8: 
>  9: def to_json(model: db.Model) -> dict:
  10:     ret = {}
  11:     for col in inspect(model).mapper.column_attrs:
```


## File controllers/api/settings.py - Line 12 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  10: @ApiRoute('settings', ApiVersion.v1)
  11: class SettingsController(BaseAPIController):
> 12:     async def get(self):
  13:         settings: Settings = self.application.digi_settings
  14:         settings_json = await settings.as_json()
```


## File controllers/ws_controller.py - Line 14 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: class WebSocketController(SessionMixin, WebSocketHandler):
  13: 
> 14:     def update_session(self):
  15:         with self.make_session() as session:
  16:             entry = session.get(Session, self.request.remote_ip)
```


## File controllers/controllers.py - Line 15 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  13: 
  14: class RootController(BaseController):
> 15:     def get(self, path):
  16:         file_path = os.path.join(
  17:             os.path.abspath(
```


## File controllers/api/settings.py - Line 17 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  11: class SettingsController(BaseAPIController):
  ...
  15:         await self.finish(settings_json)
  16: 
> 17:     async def patch(self):
  18:         settings: Settings = self.application.digi_settings
  19:
```


## File main.py - Line 22 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  20: 
  21: 
> 22: def main():
  23:     tornado.options.parse_command_line()
  24:     app = DigiScriptServer(debug=options.debug,
```


## File utils/route.py - Line 31 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: class Route(object):
  ...
  29: 
  30:     @classmethod
> 31:     def routes(cls):
  32:         return cls._routes
  33:
```


## File utils/route.py - Line 39 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  12: class Route(object):
  ...
  37: 
  38:     @classmethod
> 39:     def make(cls, _name, **kwargs):
  40:         if _name not in cls._formats:
  41:             raise KeyError('No route by the name of `{}`'.format(_name))
```


## File utils/settings.py - Line 43 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: class Settings:
  ...
  41:         }
  42: 
> 43:     async def get(self, key, default=None):
  44:         async with self.lock:
  45:             return self.settings.get(key, default)
```


## File server/app_server.py - Line 44 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  14: class DigiScriptServer(Application):
  ...
  42:             websocket_ping_interval=5)
  43: 
> 44:     def get_db(self) -> SQLAlchemy:
  45:         return self.db
```


## File controllers/controllers.py - Line 46 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  41: class ApiFallback(BaseAPIController):
  ...
  44:         self.write({'message': '404 not found'})
  45: 
> 46:     def post(self):
  47:         self.set_status(404)
  48:         self.write({'message': '404 not found'})
```


## File utils/settings.py - Line 47 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: class Settings:
  ...
  45:             return self.settings.get(key, default)
  46: 
> 47:     async def set(self, key, item):
  48:         async with self.lock:
  49:             self.settings[key] = item
```


## File controllers/controllers.py - Line 50 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  41: class ApiFallback(BaseAPIController):
  ...
  48:         self.write({'message': '404 not found'})
  49: 
> 50:     def patch(self):
  51:         self.set_status(404)
  52:         self.write({'message': '404 not found'})
```


## File utils/settings.py - Line 52 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: class Settings:
  ...
  50:             self._save()
  51: 
> 52:     async def as_json(self):
  53:         async with self.lock:
  54:             return json.loads(json.dumps(self.settings))
```


## File controllers/controllers.py - Line 54 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  41: class ApiFallback(BaseAPIController):
  ...
  52:         self.write({'message': '404 not found'})
  53: 
> 54:     def delete(self):
  55:         self.set_status(404)
  56:         self.write({'message': '404 not found'})
```


## File controllers/controllers.py - Line 69 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  67: @ApiRoute('debug', ApiVersion.v1)
  68: class ApiDebugController(BaseAPIController):
> 69:     def get(self):
  70:         self.set_status(200)
  71:         self.set_header('Content-Type', 'application/json')
```


## File controllers/api/shows.py - Line 88 - C0116 (missing-function-docstring)

- `message: Missing function or method docstring`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  86: class ShowsController(BaseAPIController):
  87: 
> 88:     def get(self):
  89:         shows = []
  90:         with self.make_session() as session:
```


# C0209: consider-using-f-string

## File utils/logger.py - Line 14 - C0209 (consider-using-f-string)

- `message: Formatting a regular string which could be a f-string`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: def add_logging_level(level_name, level_num, method_name=None):
  ...
  12:     if hasattr(logging, level_name):
  13:         raise AttributeError(
> 14:             '{} already defined in logging module'.format(level_name))
  15:     if hasattr(logging, method_name):
  16:         raise AttributeError(
```


## File utils/logger.py - Line 17 - C0209 (consider-using-f-string)

- `message: Formatting a regular string which could be a f-string`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: def add_logging_level(level_name, level_num, method_name=None):
  ...
  15:     if hasattr(logging, method_name):
  16:         raise AttributeError(
> 17:             '{} already defined in logging module'.format(method_name))
  18:     if hasattr(logging.getLoggerClass(), method_name):
  19:         raise AttributeError(
```


## File utils/logger.py - Line 20 - C0209 (consider-using-f-string)

- `message: Formatting a regular string which could be a f-string`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   8: def add_logging_level(level_name, level_num, method_name=None):
  ...
  18:     if hasattr(logging.getLoggerClass(), method_name):
  19:         raise AttributeError(
> 20:             '{} already defined in logger class'.format(method_name))
  21: 
  22:     def log_for_level(self, message, *args, **kwargs):
```


## File utils/route.py - Line 41 - C0209 (consider-using-f-string)

- `message: Formatting a regular string which could be a f-string`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  39:     def make(cls, _name, **kwargs):
  40:         if _name not in cls._formats:
> 41:             raise KeyError('No route by the name of `{}`'.format(_name))
  42:         kwargs = {k: cls._url_escape(v) for k, v in kwargs.iteritems()}
  43:         return cls._formats[_name] % kwargs
```


# C0412: ungrouped-imports

## File controllers/api/settings.py - Line 5 - C0412 (ungrouped-imports)

- `message: Imports from package controllers are not grouped`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  3: from controllers.ws_controller import WebSocketController
  4: from utils.settings import Settings
> 5: from controllers.base_controller import BaseAPIController
  6: from utils.route import ApiRoute, ApiVersion
  7: from utils.logger import get_logger
```


## File controllers/api/settings.py - Line 6 - C0412 (ungrouped-imports)

- `message: Imports from package utils are not grouped`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  4: from utils.settings import Settings
  5: from controllers.base_controller import BaseAPIController
> 6: from utils.route import ApiRoute, ApiVersion
  7: from utils.logger import get_logger
  8:
```


## File server/app_server.py - Line 7 - C0412 (ungrouped-imports)

- `message: Imports from package utils are not grouped`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   5: from utils.logger import get_logger
   6: from models.models import db, Session
>  7: from utils.route import Route
   8: from utils.settings import Settings
   9:
```


## File controllers/ws_controller.py - Line 8 - C0412 (ungrouped-imports)

- `message: Imports from package utils are not grouped`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   6: from utils.logger import get_logger
   7: from models.models import Session
>  8: from utils.route import ApiRoute, ApiVersion
   9: 
  10:
```


# R0205: useless-object-inheritance

## File utils/env_parser.py - Line 7 - R0205 (useless-object-inheritance)

- `message: Class 'EnvParser' inherits from object, can be safely removed from bases in python3`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   5: 
   6: @Singleton
>  7: class EnvParser(object):
   8: 
   9:     def __init__(self):
```


## File utils/route.py - Line 12 - R0205 (useless-object-inheritance)

- `message: Class 'Route' inherits from object, can be safely removed from bases in python3`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  10: 
  11: 
> 12: class Route(object):
  13:     """Decorator for assigning routes to Controllers"""
  14:
```


# R0903: too-few-public-methods

## File utils/env_parser.py - Line 7 - R0903 (too-few-public-methods)

- `message: Too few public methods (0/2)`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
   5: 
   6: @Singleton
>  7: class EnvParser(object):
   8: 
   9:     def __init__(self):
```


## File models/models.py - Line 24 - R0903 (too-few-public-methods)

- `message: Too few public methods (0/2)`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  22: 
  23: 
> 24: class Session(db.Model):
  25:     __tablename__ = 'sessions'
  26:
```


## File models/models.py - Line 32 - R0903 (too-few-public-methods)

- `message: Too few public methods (0/2)`
- `author : Tim Bradgate <timbradgate@hotmail.co.uk>`
- `date   : 2022-08-04T00:55:58`

```
  30: 
  31: 
> 32: class Show(db.Model):
  33:     __tablename__ = 'shows'
  34:
```

