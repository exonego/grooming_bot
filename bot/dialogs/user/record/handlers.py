from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Cancel, Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import Requests

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore

requests = Requests()


async def name_filled_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    dialog_manager.dialog_data["first_name"] = text.strip()

    i18n: TranslatorRunner = dialog_manager.middleware_data.get("i18n")
    await message.answer(
        text=i18n.record.your.name(first_name=text.strip()),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text=i18n.record.button.send.contact(), request_contact=True
                    )
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )
    await dialog_manager.next()


async def contact_sent_handler(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
) -> None:
    dialog_manager.dialog_data["phone_number"] = message.contact.phone_number

    await dialog_manager.next()


async def registration_finished_handler(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    session: AsyncSession = dialog_manager.middleware_data.get("session")
    await requests.tg_users.set_person(
        session=session,
        telegram_id=callback.from_user.id,
        first_name=dialog_manager.dialog_data.get("first_name"),
        phone_number=dialog_manager.dialog_data.get("phone_number"),
    )

    await dialog_manager.next()
