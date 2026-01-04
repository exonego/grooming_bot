from aiogram import Router

from bot.enums.roles import UserRole
from bot.filters.filters import UserRoleFilter
from .menu.dialog import menu_dialog
from .record.dialog import record_dialog

user_router = Router()
user_router.message.filter(UserRoleFilter(UserRole.USER))
user_router.callback_query.filter(UserRoleFilter(UserRole.USER))
user_router.include_routers(menu_dialog, record_dialog)


__all__ = ["user_router"]
