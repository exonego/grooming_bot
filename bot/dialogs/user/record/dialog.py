from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.input import TextInput

from bot.states.states import RecordSG
from bot.dialogs.user.record.getters import get_fill_name_window
from bot.dialogs.user.record.handlers import (
    name_filled_handler,
    record_cancelled_handler,
)


record_dialog = Dialog(
    Window(
        Format(text="{record_registration}", when="is_first_name"),
        Format(text="{record_fill_name}"),
        Cancel(
            text=Format("{cancel_button}"),
            id="cancel_registration",
            on_click=record_cancelled_handler,
        ),
        TextInput(id="first_name_input", on_success=name_filled_handler),
        getter=get_fill_name_window,
        state=RecordSG.fill_name,
    ),
)
