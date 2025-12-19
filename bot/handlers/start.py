import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from fluentogram import TranslatorRunner

from infrastructure.database import Requests, TgUser
from bot.enums.roles import UserRole

if TYPE_CHECKING:
    from I18N import TranslatorRunner

requests = Requests()
start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(
    message: Message,
    session: AsyncSession,
    i18n: TranslatorRunner,
    db_user: TgUser,
    user_role: UserRole,
):
    """Reacts to /start"""
    if user_role == UserRole.USER:
        if db_user is None or db_user.first_name is None:
            await message.answer(text=i18n.cmd.start.left())
        else:
            await message.answer(
                text=i18n.cmd.start.user(first_name=db_user.first_name)
            )
    else:
        await message.answer(text=i18n.cmd.start.admin())

    if db_user is None:
        await requests.tg_users.add_user(
            session=session,
            telegram_id=message.from_user.id,
            language=message.from_user.language_code,
            role=user_role,
        )
