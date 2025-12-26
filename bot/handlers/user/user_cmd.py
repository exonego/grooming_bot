import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from bot.enums.roles import UserRole
from bot.filters.filters import UserRoleFilter
from bot.states.states import RecordSG
from bot.dialogs.user.record.dialog import record_dialog
from infrastructure.database import TgUser


if TYPE_CHECKING:
    from I18N import TranslatorRunner

logger = logging.getLogger(__name__)

user_cmd_router = Router()
user_cmd_router.message.filter(UserRoleFilter(UserRole.USER))
user_cmd_router.include_routers(record_dialog)


@user_cmd_router.message(Command("record"))
async def cmd_record(
    message: Message,
    db_user: TgUser,
    dialog_manager: DialogManager,
):
    if db_user.first_name is None:
        await dialog_manager.start(state=RecordSG.fill_name, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(
            state=RecordSG.choose_pet,
            mode=StartMode.RESET_STACK,
            data={"is_first_name": True},
        )
