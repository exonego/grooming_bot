from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from I18N.locales.stub import TranslatorRunner  # type: ignore


async def menu_getter(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs):
    return {
        "menu_text": i18n.menu.text(
            first_name=dialog_manager.start_data.get("first_name")
        ),
        "menu_button_record": i18n.menu.button.record(),
    }
