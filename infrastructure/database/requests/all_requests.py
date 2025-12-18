from dataclasses import dataclass, field

from . import tg_users


@dataclass
class TgUsers:
    @property
    def get_user(self):
        return tg_users.get_user


@dataclass
class Requests:
    tg_users: TgUsers = field(default_factory=TgUsers)
