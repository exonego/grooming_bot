from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore


async def fill_name_getter(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, str]:
    return {
        "record_fill_name": i18n.record.fill.name(),
        "button_cancel": i18n.button.cancel(),
    }


async def send_contact_getter(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, str]:
    return {
        "record_send_contact": i18n.record.send.contact(),
        "button_cancel": i18n.button.cancel(),
        "button_back": i18n.button.back(),
    }
