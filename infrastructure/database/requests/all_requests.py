from dataclasses import dataclass, field

from . import tg_users


@dataclass
class TgUsers:
    @property
    def get_user(self):
        return tg_users.get_user

    @property
    def add_user(self):
        return tg_users.add_user

    @property
    def set_role(self):
        return tg_users.set_role


@dataclass
class Requests:
    tg_users: TgUsers = field(default_factory=TgUsers)
