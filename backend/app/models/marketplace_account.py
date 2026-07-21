from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from app.database.base import Base


class MarketplaceAccount(Base):
    __tablename__ = "marketplace_accounts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False
    )

    platform: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    account_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    seller_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    access_token = mapped_column(
        Text,
        nullable=True
    )

    refresh_token = mapped_column(
        Text,
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    last_sync: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    company: Mapped["Company"] = relationship(
        back_populates="marketplace_accounts"
    )

    product_marketplaces: Mapped[list["ProductMarketplace"]] = relationship(
        back_populates="marketplace_account",
        cascade="all, delete-orphan"
    )