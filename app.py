import os
from core.router import CoreRouter
from flask_cors import CORS
from flask import Flask


def initialize_app():
    _app = Flask(__name__)
    core_router = CoreRouter(_app)
    core_router.get("/", lambda: "SF Botmart Running")
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
