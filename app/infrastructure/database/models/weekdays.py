from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base

if TYPE_CHECKING:
    from .record_dates import RecordDate


class Weekday(Base):
    __tablename__ = "weekdays"

    num: Mapped[int] = mapped_column(Integer, primary_key=True)
    blocked: Mapped[str] = mapped_column(Text, nullable=True, default=None)

    record_dates: Mapped[list[RecordDate]] = relationship(
        back_populates="weekday", cascade="delete", lazy="selectin"
    )
