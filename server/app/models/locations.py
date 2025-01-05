from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.database import Model


class Location(Model):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped["LocationType"] = relationship(back_populates="locations")
    country: Mapped["Country"] = relationship(back_populates="locations")
    name: Mapped[str] = mapped_column(String(300), index=True)
    latitude: Mapped[float]
    longitude: Mapped[float]
