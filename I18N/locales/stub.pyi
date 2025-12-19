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
    def left() -> Literal["""&lt;b&gt;Здравствуйте, вы написали в Зоорум ЗооВайб!&lt;/b&gt;\n
Для записи отправьте /record"""]: ...
    @staticmethod
    def user(*, first_name: PossibleValue) -> Literal["""&lt;b&gt;Здравствуйте, { $first_name }!&lt;/b&gt;\n\n
Для записи отправьте /record"""]: ...
    @staticmethod
    def admin() -> Literal["""&lt;/b&gt;Здравствуйте, Администратор!&lt;/b&gt;\n\n"""]: ...

class Cmd:
    start: CmdStart
