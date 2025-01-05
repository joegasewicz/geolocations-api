from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.database import Model


class Country(Model):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)

    def __repr__(self):
        return f"Country({self.id}, {self.name})"
