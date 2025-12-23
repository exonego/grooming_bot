from decimal import Decimal
from typing import Literal

from fluent_compiler.types import FluentType
from typing_extensions import TypeAlias

PossibleValue: TypeAlias = str | int | float | Decimal | bool | FluentType

class TranslatorRunner:
    def get(self, path: str, **kwargs: PossibleValue) -> str: ...
    cmd: Cmd
    record: Record

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

class RecordFill:
    @staticmethod
    def name() -> Literal["""&lt;b&gt;Пожалуйста, введите ваше имя (Только кириллица, без пробелов)&lt;/b&gt;
Для отмены отправьте /cancel"""]: ...

class Record:
    fill: RecordFill

    @staticmethod
    def registration() -> Literal["""Пройдите пожалуйста небольшую регистрацию прежде чем мы вас запишем"""]: ...
