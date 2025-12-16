from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import BigInteger, Text, Boolean, DateTime, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base

if TYPE_CHECKING:
    from .records import Record


class TgUser(Base):
    __tablename__ = "tg_users"
    __table_args__ = (
        Index("idx_tg_users_tg_id", "tg_id"),
        Index("idx_tg_users_phone_number", "phone_number"),
    )

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

    records: Mapped[list[Record]] = relationship(
        back_populates="tg_user", cascade="delete", lazy="selectin"
    )
