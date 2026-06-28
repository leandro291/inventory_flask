from db import db
from sqlalchemy import Integer, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Inventory(db.Model):
    
    __tablename__ = "inventories"

    id_inventory: Mapped[int] = mapped_column(Integer, primary_key=True)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    id_product: Mapped[int] = mapped_column(ForeignKey('products.id_product'), nullable=False)
    id_repository: Mapped[int] = mapped_column(ForeignKey('repositories.id_repository'), nullable=False)
