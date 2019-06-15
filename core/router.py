from flask import Flask
from typing import Callable, List, Type
from .middleware import Middleware
from .exception.core_build_exception import CoreServerException


class _BaseRouter:
    def __init__(self):
        self._routes = {}

    def group(self, prefix: str, router: "Router", *middleware: Middleware):
        routes = router._routes

        for key, value in routes.items():
            handler = value
            endpoint, methods = key
            self.__add_middleware(handler, [instance for instance in middleware])
            self._routes[(prefix + endpoint, methods)] = handler

            # TODO: need to remove this code if success
            # method, handler = value
            # self.add_middleware(handler, middleware)
            # try:
            #     method = getattr(self, method.lower())
            #     method(prefix + key, handler)
            # except AttributeError:
            #     raise CoreException("HTTP Method not detected. Only GET, POST, PUT, DELETE can be given")

    def get(self, endpoint: str, *handlers: Callable):
        self._routes[(endpoint, "GET")] = self.__generate_route_handler(handlers)

    def post(self, endpoint: str, *handlers: Callable):
        self._routes[(endpoint, "POST")] = self.__generate_route_handler(handlers)

    def put(self, endpoint: str, *handlers: Callable):
        self._routes[(endpoint, "PUT")] = self.__generate_route_handler(handlers)

    def delete(self, endpoint: str, *handlers: Callable):
        self._routes[(endpoint, "DELETE")] = self.__generate_route_handler(handlers)

    def route(self, endpoint: str, methods: List[str], *handlers: Callable):
        accepted_methods = ["GET", "POST", "PUT", "DELETE"]

        if not all(method.upper() in accepted_methods for method in methods):
            raise CoreServerException("Method not accepted")

        if len(methods) == 0:
            raise CoreServerException("No method given")

        self._routes[
            (endpoint, "_".join(methods).upper())
        ] = self.__generate_route_handler(handlers)

    @classmethod
    def __add_middleware(cls, handler: Callable, middleware: List[Middleware]):
        for instance in middleware:
            if issubclass(type(instance), Middleware):
                handler = instance.add_next(handler)
            else:
                raise CoreServerException(
                    "Only class which inherits Middleware can be given as parameter"
                )
        return handler

    @classmethod
    def __generate_route_handler(cls, handlers):
        len_handlers = len(handlers)

        if len_handlers == 1:
            handler = handlers[0]

            if not callable(handler):
                raise CoreServerException("Not a callable")

            return handlers[0]
        elif len_handlers > 1:
            handler = handlers[len_handlers - 1]
            middleware = handlers[: (len_handlers - 1)]

            if not callable(handler):
                raise CoreServerException("Not a callable")

            return cls.__add_middleware(handler, middleware[::-1])

        raise CoreServerException("No handler given.")


class CoreRouter(_BaseRouter):
    def __init__(self, app: Flask):
        super().__init__()
        self.app = app

    def execute(self):
        for key, handler in self._routes.items():
            endpoint, req_types = key
            name = endpoint + req_types
            methods = req_types.upper().split("_")
            self.app.route(
                endpoint, endpoint=name, methods=methods, strict_slashes=False
            )(handler)

    def add_error_handler(self, class_type: Type[Exception], handler: Callable):
        self.app.register_error_handler(class_type, handler)


class Router(_BaseRouter):
    def __int__(self):
        super().__init__()
