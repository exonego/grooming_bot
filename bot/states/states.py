from aiogram.fsm.state import State, StatesGroup


class RecordSG(StatesGroup):
    fill_name = State()
    send_contact = State()
    register = State()

    choose_pet = State()
    choose_weight = State()
    choose_service = State()
    fill_date = State()
    choose_time = State()
    confirm = State()
