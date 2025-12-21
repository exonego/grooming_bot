import logging

from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from bot.enums.roles import UserRole

logger = logging.getLogger(__name__)


class UserRoleFilter(BaseFilter):
    """Checks the user_role"""

    def __init__(self, *roles: str | UserRole):
        if not roles:
            raise ValueError("At least one role must be passed to UserRoleFilter")

        self.roles = frozenset(
            UserRole(role) if isinstance(role, str) else role
            for role in roles
            if isinstance(role, (str, UserRole))
        )

        if not self.roles:
            raise ValueError("No valid roles passed to UserRoleFilter")

    async def __call__(
        self, event: Message | CallbackQuery, user_role: UserRole
    ) -> bool:

        user = event.from_user
        if user is None:
            return False

        return user_role in self.roles
