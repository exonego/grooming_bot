from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from fluentogram import TranslatorRunner

from bot.states.states import RecordSG
from infrastructure.database import TgUser

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore


async def record_clicked_handler(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    db_user: TgUser = dialog_manager.middleware_data.get("db_user")

    if db_user.first_name is None:
        await dialog_manager.start(
            state=RecordSG.fill_name,
        )
    else:
        await dialog_manager.start(
            state=RecordSG.choose_pet,
        )
