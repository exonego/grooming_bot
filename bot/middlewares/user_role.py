import logging
from collections.abc import Callable, Awaitable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import Update, User

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import Requests, TgUser
from bot.enums.roles import UserRole

logger = logging.getLogger(__name__)
requests = Requests()


class UserRoleMiddleware(BaseMiddleware):
    """Middleware which drops user's role into the context."""

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ) -> Any:

        user: User = data.get("event_from_user")
        if user is None:
            return await handler(event, data)

        admin_id: int = data.get("admin_id")
        session: AsyncSession = data.get("session")

        db_user: TgUser = data.get("db_user")

        if db_user is None:

            if user.id != admin_id:
                data["user_role"] = UserRole.USER
                return await handler(event, data)
            else:
                data["user_role"] = UserRole.ADMIN
        else:

            if db_user.role == UserRole.ADMIN and user.id != admin_id:
                await requests.tg_users.set_role(
                    session=session, telegram_id=user.id, role=UserRole.USER
                )
                data["user_role"] = UserRole.USER
            elif db_user.role == UserRole.USER and user.id == admin_id:
                await requests.tg_users.set_role(
                    session=session, telegram_id=user.id, role=UserRole.ADMIN
                )
                data["user_role"] = UserRole.ADMIN
            else:
                data["user_role"] = db_user.role

        return await handler(event, data)
