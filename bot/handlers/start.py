import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession
from fluentogram import TranslatorRunner

from infrastructure.database import Requests, TgUser
from bot.enums.roles import UserRole
from bot.states.states import UserMenuSG

if TYPE_CHECKING:
    from I18N import TranslatorRunner

logger = logging.getLogger(__name__)

requests = Requests()
start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(
    message: Message,
    dialog_manager: DialogManager,
    session: AsyncSession,
    i18n: TranslatorRunner,
    db_user: TgUser | None,
    user_role: UserRole,
):
    """Reacts to /start"""
    if db_user is None:
        await requests.tg_users.add_user(
            session=session,
            telegram_id=message.from_user.id,
            language=message.from_user.language_code,
            role=user_role,
        )

    if user_role == UserRole.USER:
        await dialog_manager.start(
            state=UserMenuSG.menu,
            mode=StartMode.RESET_STACK,
            data={
                "first_name": (
                    "unknown"
                    if db_user is None or db_user.first_name is None
                    else db_user.first_name
                )
            },
        )
    else:
        pass
