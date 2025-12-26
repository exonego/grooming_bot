from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.input import ManagedTextInput
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore


async def record_cancelled_handler(
    callback: CallbackQuery, button: Cancel, dialog_manager: DialogManager
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get("i18n")
    await callback.message.answer(text=i18n.record.registration.cancelled())


async def name_filled_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    dialog_manager.dialog_data["first_name"] = text.strip()
    dialog_manager.dialog_data["is_first_name"] = False

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
