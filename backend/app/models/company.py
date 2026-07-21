from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    corporate_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    trade_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    cnpj: Mapped[str] = mapped_column(
        String(18),
        unique=True,
        nullable=False
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

    marketplace_accounts: Mapped[list["MarketplaceAccount"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan"
    )

    product_companies: Mapped[list["ProductCompany"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan"
    )