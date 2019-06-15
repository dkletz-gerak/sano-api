from core.router import Router
from src.route.user import user_router
from src.route.category import category_router

group_router = Router()
group_router.group("/user", user_router)
group_router.group("/category", category_router)

__all__ = [group_router]
