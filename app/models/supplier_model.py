from db import db
from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Supplier(db.Model):

    __tablename__ = "suppliers"

    id_supplier: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False)
    telephone: Mapped[str] = mapped_column(String(15), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    id_company: Mapped[int] = mapped_column(ForeignKey('companies.id_company'), nullable=False)
