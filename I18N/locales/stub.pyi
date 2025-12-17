from decimal import Decimal
from typing import Literal

from fluent_compiler.types import FluentType
from typing_extensions import TypeAlias

PossibleValue: TypeAlias = str | int | float | Decimal | bool | FluentType

class TranslatorRunner:
    def get(self, path: str, **kwargs: PossibleValue) -> str: ...
    cmd: Cmd

class CmdStart:
    @staticmethod
    def left() -> Literal["""Здравствуйте, вы написали в Зоорум ЗооВайб!\n
&lt;b&gt;Для записи отправьте /record&lt;/b&gt;"""]: ...
    @staticmethod
    def user(*, first_name: PossibleValue) -> Literal["""Здравствуйте, { $first_name }!\n
&lt;b&gt;Для записи отправьте /record&lt;/b&gt;"""]: ...

class Cmd:
    start: CmdStart
