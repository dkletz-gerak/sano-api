import os
from src import model


HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))
THREADED = os.getenv("THREADED", "TRUE") == "TRUE"
DEBUG = os.getenv("DEBUG", "TRUE") == "TRUE"

MODEL_PATH = "src/model/__init__.py"
MODEL = model.__all__
