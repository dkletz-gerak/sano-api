import os
from src import model


HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))
THREADED = os.getenv("THREADED", "TRUE") == "TRUE"
DEBUG = os.getenv("DEBUG", "TRUE") == "TRUE"

MODEL = [model.__all__]
