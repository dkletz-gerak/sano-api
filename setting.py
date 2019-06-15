import core.load_env
import os
from src import model
import logging


HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))
THREADED = os.getenv("THREADED", "TRUE") == "TRUE"
DEBUG = os.getenv("DEBUG", "TRUE") == "TRUE"

MODEL_PATH = "src/model/__init__.py"
MODEL = model.__all__

if DEBUG:
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
