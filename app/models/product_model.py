from db import db
from sqlalchemy import Integer, String, Text, DECIMAL, DateTime, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Product(db.Model):
    
    __tablename__ = "products"

    id_product: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(7), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(Text, nullable=False)
    brand: Mapped[str] = mapped_column(String(255), nullable=False)
    purhcase_price: Mapped[float] = mapped_column(DECIMAL(10,4), nullable=False)
    sale_price: Mapped[float] = mapped_column(DECIMAL(10,4), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    id_category: Mapped[int] = mapped_column(ForeignKey('categories.id_category'), nullable=False)

