from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import BigInteger, Text, DateTime, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base

if TYPE_CHECKING:
    from .records import Record


class PhoneClient(Base):
    __tablename__ = "phone_clients"
    __table_args__ = (
        Index("idx_phone_clients_id", "id"),
        Index("idx_phone_clients_phone_number", "phone_number")
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=False)
    phone_number: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    records: Mapped[list[Record]] = relationship(
        back_populates="phone_client", cascade="delete", lazy="selectin"
    )
