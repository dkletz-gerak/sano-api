import os

from core.exception.core_http_exception import CoreHttpException
from core.router import CoreRouter
from flask_cors import CORS
from flask import Flask
from src.admin import views
from src.exception.exception_handler import *
from src.route import group_router


def add_error_handler(core_router):
    core_router.add_error_handler(CoreHttpException, handle_general_exception)
    core_router.add_error_handler(Exception, handle_other_exception)
    core_router.add_error_handler(404, handle_page_not_found)
    core_router.add_error_handler(405, handle_method_not_allowed)


def initialize_app():
    _app = Flask(__name__)
    _app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    core_router = CoreRouter(_app)
    core_router.get("/", lambda: "SF Botmart Running")
    core_router.group("", group_router)
    add_error_handler(core_router)
    core_router.set_admin()
    core_router.add_admin_views(views)
    CORS(_app)
    core_router.execute()
    return _app


app = initialize_app()


if __name__ == "__main__":
    app.run(
        port=int(os.getenv("PORT")),
        host=os.getenv("HOST"),
        threaded=True,
        debug=os.getenv("DEBUG"),
    )
