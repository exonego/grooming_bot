from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date, time, datetime

from sqlalchemy import (
    BigInteger,
    Text,
    Date,
    Time,
    DateTime,
    ForeignKey,
    func,
    Index,
    CheckConstraint,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from .tg_users import TgUser
    from .phone_clients import PhoneClient
    from .record_dates import RecordDate


class Record(Base):
    __tablename__ = "records"
    __table_args__ = (
        Index("idx_records_tg_user_id", "tg_user_id"),
        Index("idx_records_phone_client_id", "phone_client_id"),
        Index("idx_records_day", "day"),
        Index("idx_records_r_time", "r_time"),
        CheckConstraint(
            "tg_user_id IS NOT NULL OR phone_client_id IS NOT NULL",
            name="phone_or_tg_id_is_not_null",
        ),
        UniqueConstraint("day", "r_time", name="unique_record_datetime"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    tg_user_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("tg_users.tg_id", ondelete="CASCADE"),
        nullable=True,
        default=None,
    )
    phone_client_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("phone_clients.id", ondelete="CASCADE"),
        nullable=True,
        default=None,
    )
    gr_service: Mapped[str] = mapped_column(Text, nullable=False)
    day: Mapped[date] = mapped_column(
        Date, ForeignKey("record_dates.day", ondelete="CASCADE"), nullable=False
    )
    r_time: Mapped[time] = mapped_column(Time, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    tg_user: Mapped[TgUser] = relationship(back_populates="records", lazy="joined")
    phone_client: Mapped[PhoneClient] = relationship(
        back_populates="records", lazy="joined"
    )
    record_date: Mapped[RecordDate] = relationship(
        back_populates="records", lazy="joined"
    )
