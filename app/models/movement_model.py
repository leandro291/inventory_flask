from db import db
from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Movement(db.Model):
    
    __tablename__ = "movements"

    id_movement: Mapped[int] = mapped_column(Integer, primary_key=True)
    observation: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    id_supplier: Mapped[int] = mapped_column(ForeignKey('suppliers.id_supplier'), nullable=False)
    id_type_movement: Mapped[int] = mapped_column(ForeignKey('type_movements.id_type_movement'), nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id_user'), nullable=False)
    id_repository: Mapped[int] = mapped_column(ForeignKey('repositories.id_repository'), nullable=False)
