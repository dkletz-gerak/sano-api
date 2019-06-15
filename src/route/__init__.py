from core.router import Router
from src.route.user import user_router

group_router = Router()
group_router.group("/user", user_router)

__all__ = [group_router]
