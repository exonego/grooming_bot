from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import Date, Text, Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database import Base

if TYPE_CHECKING:
    from .weekdays import Weekday
    from .records import Record


class RecordDate(Base):
    __tablename__ = "record_dates"
    __table_args__ = (
        Index("idx_record_dates_day", "day"),
        Index("idx_record_dates_weekday_num", "weekday_num"),
    )

    day: Mapped[date] = mapped_column(Date, primary_key=True)
    blocked: Mapped[str | None] = mapped_column(Text, nullable=True)
    weekday_num: Mapped[int] = mapped_column(Integer, ForeignKey("weekdays.num"))

    weekday: Mapped[Weekday] = relationship(
        back_populates="record_dates", lazy="joined"
    )
    records: Mapped[list[Record]] = relationship(
        back_populates="record_date", cascade="delete", lazy="selectin"
    )
