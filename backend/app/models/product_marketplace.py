from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductMarketplace(Base):
    __tablename__ = "product_marketplaces"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    product_company_id: Mapped[int] = mapped_column(
        ForeignKey("product_companies.id"),
        nullable=False
    )

    marketplace_account_id: Mapped[int] = mapped_column(
        ForeignKey("marketplace_accounts.id"),
        nullable=False
    )

    marketplace_product_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    marketplace_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="active"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
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

    product_company: Mapped["ProductCompany"] = relationship(
        back_populates="product_marketplaces"
    )

    marketplace_account: Mapped["MarketplaceAccount"] = relationship(
        back_populates="product_marketplaces"
    )

    metrics: Mapped[list["Metric"]] = relationship(
        back_populates="product_marketplace",
        cascade="all, delete-orphan"
    )