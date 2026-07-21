from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Metric(Base):
    __tablename__ = "metrics"

    __table_args__ = (
        UniqueConstraint(
            "product_marketplace_id",
            "metric_date",
            name="uq_metric_day"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    product_marketplace_id: Mapped[int] = mapped_column(
        ForeignKey("product_marketplaces.id"),
        nullable=False,
        index=True
    )

    metric_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    visits: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    sales: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    revenue: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0
    )

    questions: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    favorites: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    available_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    product_marketplace: Mapped["ProductMarketplace"] = relationship(
        back_populates="metrics"
    )