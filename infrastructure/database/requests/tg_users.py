from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import TgUser
from bot.enums.roles import UserRole


async def get_user(session: AsyncSession, telegram_id: int) -> TgUser:
    "Returns TgUser by telegram_id"
    return await session.get(TgUser, telegram_id)


async def add_user(
    session: AsyncSession,
    telegram_id: int,
    language: str,
    role: UserRole = UserRole.USER,
    first_name: str | None = None,
    phone_number: str | None = None,
) -> None:

    new_user = TgUser(
        tg_id=telegram_id,
        first_name=first_name,
        phone_number=phone_number,
        role=role,
        language=language,
    )

    session.add(new_user)
    await session.commit()


async def set_role(
    session: AsyncSession,
    telegram_id: int,
    role: UserRole,
) -> None:

    user = await session.get(TgUser, telegram_id)
    user.role = role
    await session.commit()


async def set_person(
    session: AsyncSession,
    telegram_id: int,
    first_name: str,
    phone_number: str,
) -> None:
    stmt = select(TgUser).where(TgUser.tg_id == telegram_id)
    result = await session.execute(stmt)
    tg_user = result.scalar()

    tg_user.first_name = first_name
    tg_user.phone_number = phone_number
    await session.commit()
