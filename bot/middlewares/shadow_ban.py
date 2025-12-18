import logging
from collections.abc import Callable, Awaitable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import Update, User
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import Requests

logger = logging.getLogger(__name__)

requests = Requests()


class ShadowBanMiddleware(BaseMiddleware):
    """Middleware which blocks updates from a banned user"""

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ) -> Any:

        user: User = data.get("event_from_user")
        if user is None:
            return await handler(event, data)

        session: AsyncSession = data.get("session")

        db_user = await requests.tg_users.get_user(session=session, telegram_id=user.id)
        data["db_user"] = db_user

        if db_user and db_user.banned:
            if event.callback_query:
                await event.callback_query.answer()
            return

        return await handler(event, data)
