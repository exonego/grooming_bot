from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import TgUser


async def get_user(session: AsyncSession, telegram_id: int) -> TgUser:
    "Returns TgUser by telegram_id"
    return await session.get(TgUser, telegram_id)
