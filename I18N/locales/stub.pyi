from decimal import Decimal
from typing import Literal

from fluent_compiler.types import FluentType
from typing_extensions import TypeAlias

PossibleValue: TypeAlias = str | int | float | Decimal | bool | FluentType

class TranslatorRunner:
    def get(self, path: str, **kwargs: PossibleValue) -> str: ...
    button: Button
    record: Record
    cmd: Cmd

class Button:
    @staticmethod
    def back() -> Literal["""◀️ Назад"""]: ...
    @staticmethod
    def cancel() -> Literal["""❌ Отмена"""]: ...
    @staticmethod
    def confirm() -> Literal["""✅ Подтвердить"""]: ...

class RecordRegistration:
    @staticmethod
    def start() -> Literal["""Пройдите пожалуйста небольшую регистрацию прежде чем мы вас запишем"""]: ...
    @staticmethod
    def completed() -> Literal["""Регистрация успешно завершена!"""]: ...
    @staticmethod
    def cancelled() -> Literal["""Регистрация прервана."""]: ...

class RecordFill:
    @staticmethod
    def name() -> Literal["""&lt;b&gt;Введите ваше имя&lt;/b&gt;"""]: ...

class RecordYour:
    @staticmethod
    def name(*, first_name: PossibleValue) -> Literal["""Ваше имя: { $first_name }"""]: ...

class RecordSend:
    @staticmethod
    def contact() -> Literal["""&lt;b&gt;Отправьте контакт, нажав на кнопку внизу&lt;/b&gt;"""]: ...

class RecordButtonSend:
    @staticmethod
    def contact() -> Literal["""☎️ Отправить контакт"""]: ...

class RecordButtonPet:
    @staticmethod
    def cat() -> Literal["""😺 Кот/кошка"""]: ...
    @staticmethod
    def dog() -> Literal["""🐶 Пес/собака"""]: ...

class RecordButton:
    send: RecordButtonSend
    pet: RecordButtonPet

class RecordChoose:
    @staticmethod
    def pet() -> Literal["""&lt;b&gt;Какой у вас питомец?&lt;/b&gt;"""]: ...

class Record:
    registration: RecordRegistration
    fill: RecordFill
    your: RecordYour
    send: RecordSend
    button: RecordButton
    choose: RecordChoose

    @staticmethod
    def register(*, first_name: PossibleValue, phone_number: PossibleValue) -> Literal["""&lt;b&gt;Ваше имя: { $first_name }&lt;/b&gt;
&lt;b&gt;Ваш номер телефона: { $phone_number }&lt;/b&gt;

&lt;b&gt;&lt;i&gt;Подтвердить регистрацию?&lt;/i&gt;&lt;/b&gt;"""]: ...

class CmdStart:
    @staticmethod
    def left() -> Literal["""&lt;b&gt;Здравствуйте, вы написали в Зоорум ЗооВайб!&lt;/b&gt;


Для записи отправьте /record"""]: ...
    @staticmethod
    def user(*, first_name: PossibleValue) -> Literal["""&lt;b&gt;Здравствуйте, { $first_name }!&lt;/b&gt;


Для записи отправьте /record"""]: ...
    @staticmethod
    def admin() -> Literal["""&lt;b&gt;Здравствуйте, Администратор!&lt;/b&gt;"""]: ...

class Cmd:
    start: CmdStart
