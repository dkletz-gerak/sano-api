from src.controller.user import *
from src.middleware.auth import AuthMiddleware
from core.router import Router


# Normal user for sano
user_router = Router()
user_router.post("/login", login)
user_router.post("/register", register)
user_router.get("/profile", AuthMiddleware(), get_profile)
