from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button

from bot.states.states import UserMenuSG
from bot.dialogs.user.menu.getters import menu_getter
from bot.dialogs.user.menu.handlers import record_clicked_handler


menu_dialog = Dialog(
    Window(
        Format(text="{menu_text}"),
        Button(
            text=Format("{menu_button_record}"),
            id="record",
            on_click=record_clicked_handler,
        ),
        getter=menu_getter,
        state=UserMenuSG.menu,
    )
)
