from typing import TYPE_CHECKING, Any

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore


async def get_fill_name_window(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs
) -> dict[str, Any]:
    return {
        "record_registration": i18n.record.registration(),
        "record_fill_name": i18n.record.fill.name(),
        "cancel_button": i18n.button.cancel(),
        "is_first_name": dialog_manager.dialog_data.get("is_first_name"),
    }
