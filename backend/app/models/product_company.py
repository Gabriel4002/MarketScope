from __future__ import annotations

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductCompany(Base):
    __tablename__ = "product_companies"

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "company_id",
            name="uq_product_company"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    product: Mapped["Product"] = relationship(
        back_populates="product_companies"
    )

    company: Mapped["Company"] = relationship(
        back_populates="product_companies"
    )

    product_marketplaces: Mapped[list["ProductMarketplace"]] = relationship(
        back_populates="product_company",
        cascade="all, delete-orphan"
    )