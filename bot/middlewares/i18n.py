import logging
from collections.abc import Callable, Awaitable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import Update, User
from fluentogram import TranslatorHub

from infrastructure.database import TgUser

logger = logging.getLogger(__name__)


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ) -> Any:

        user: User = data.get("event_from_user")

        if user is None:
            return await handler(event, data)

        db_user: TgUser = data.get("db_user")
        if db_user:
            user_lang = db_user.language
        else:
            user_lang = user.language_code

        hub: TranslatorHub = data.get("_translator_hub")
        data["i18n"] = hub.get_translator_by_locale(locale=user_lang)

        return await handler(event, data)
