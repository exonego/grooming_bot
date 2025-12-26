from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Cancel, Back, Row
from aiogram_dialog.widgets.input import TextInput, MessageInput

from bot.states.states import RecordSG
from bot.dialogs.user.record.getters import fill_name_getter, send_contact_getter
from bot.dialogs.user.record.handlers import (
    registration_cancelled_handler,
    name_filled_handler,
    contact_sent_handler,
)


cancel_registration_widget = Cancel(
    text=Format(text="{button_cancel}"),
    id="cancel_registration",
    on_click=registration_cancelled_handler,
)
back_widget = Back(text=Format(text="{button_back}"))


record_dialog = Dialog(
    Window(
        Format(text="{record_fill_name}"),
        cancel_registration_widget,
        TextInput(id="first_name_input", on_success=name_filled_handler),
        getter=fill_name_getter,
        state=RecordSG.fill_name,
    ),
    Window(
        Format(text="{record_send_contact}"),
        Row(
            cancel_registration_widget,
            back_widget,
        ),
        MessageInput(func=contact_sent_handler, content_types=ContentType.CONTACT),
        getter=send_contact_getter,
        state=RecordSG.send_contact,
    ),
)
