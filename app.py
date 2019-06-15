import os
from core.router import CoreRouter
from flask_cors import CORS
from flask import Flask
from src.admin import views


def initialize_app():
    _app = Flask(__name__)
    _app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    core_router = CoreRouter(_app)
    core_router.get("/", lambda: "SF Botmart Running")
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
