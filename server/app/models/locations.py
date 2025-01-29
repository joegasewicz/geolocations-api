"""
Column("id", Integer, primary_key=True),
        Column("town", String(255)),
        Column("longitude", Float(8)),
        Column("latitude", Float(8)),
        Column("iso_3166_1", String(255)),
        Column("country", String(255)),
"""
from sqlalchemy import (
    Float,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.utils.database import Model


class Location(Model):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    # location: Mapped["LocationType"] = relationship(back_populates="locations") TODO
    # country: Mapped["Country"] = relationship(back_populates="locations") TODO
    town: Mapped[str] = mapped_column(String(255), index=True)
    latitude: Mapped[float] = mapped_column(Float(8))
    longitude: Mapped[float] = mapped_column(Float(8))
    country: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return (f"Location("
                f"{self.id}, "
                f"{self.town}, "
                f"{self.latitude}, "
                f"{self.longitude}, "
                f"{self.country})")
