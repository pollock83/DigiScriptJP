from enum import Enum
import urllib.parse

from tornado.web import URLSpec
import tornado.escape
from tornado.websocket import WebSocketHandler

from utils.web.base_controller import BaseAPIController


class Route:
    """Decorator for assigning routes to Controllers"""

    _routes = []
    _formats = {}

    def __init__(self, route, name=None):
        self.route = route
        self.name = name
        self._formats[name] = route

    def __call__(self, controller):
        name = self.name or controller.__name__
        controller._route_name = name
        url_spec = URLSpec(self.route, controller, name=name)
        self._routes.append(url_spec)
        return controller

    @classmethod
    def routes(cls):
        return cls._routes

    @staticmethod
    def _url_escape(url):
        return urllib.parse.quote(tornado.escape.utf8(url), '')

    @classmethod
    def make(cls, _name, **kwargs):
        if _name not in cls._formats:
            raise KeyError(f'No route by the name of `{_name}`')
        kwargs = {k: cls._url_escape(v) for k, v in kwargs.items()}
        return cls._formats[_name] % kwargs


class ApiVersion(Enum):
    V1 = 1


class ApiRoute(Route):
    def __init__(self, route: str, api_version: ApiVersion, name: str = None):
        route = f'/api/v{api_version.value}/{route.removeprefix("/")}'
        super().__init__(route, name)

    def __call__(self, controller):
        if not issubclass(controller, (BaseAPIController, WebSocketHandler)):
            raise RuntimeError(
                f'Controller class {controller.__name__} is not an '
                f'instance of BaseAPIController or WebSocketHandler')
        super().__call__(controller)