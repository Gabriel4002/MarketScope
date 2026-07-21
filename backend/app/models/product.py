from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    brand: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True
    )

    gtin: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    internal_category: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
        nullable=False
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

    product_companies: Mapped[list["ProductCompany"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    history: Mapped[list["History"]] = relationship(
        back_populates="product"
    )