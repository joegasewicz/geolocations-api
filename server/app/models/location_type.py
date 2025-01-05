from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.utils.database import Model


class LocationType(Model):
    __tablename__ = "location_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))

    def __repr__(self):
        return f"LocationType({self.id}, {self.name})"
