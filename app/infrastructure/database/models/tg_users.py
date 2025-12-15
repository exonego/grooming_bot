from datetime import datetime

from sqlalchemy import BigInteger, Text, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class TgUser(Base):
    __tablename__ = "tg_users"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=False)
    phone_number: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(Text, nullable=False)
    language: Mapped[str] = mapped_column(Text, nullable=False)
    banned: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_alive: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
