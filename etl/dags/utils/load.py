from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import (
    create_engine,
    types,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Float,
)
from sqlalchemy.engine import Engine
from pandas import DataFrame


class Load:

    engine: Engine
    df_dict: DataFrame
    file_path: str
    __table_name__ = "locations"

    def __init__(self, *, engine: Engine, df_dict: DataFrame, file_path: str):
        self.engine = engine
        self.df_dict = df_dict
        self.file_path = file_path

    def run(self):
        metadata = MetaData()
        locations_table = Table(self.__table_name__, metadata,
            Column("id", Integer, primary_key=True),
            Column("town", String(255)),
            Column("longitude", Float(8)),
            Column("latitude", Float(8)),
            Column("country", String(255)),
        )
        try:
            with self.engine.connect() as conn:
                metadata.create_all(conn)
                df_dict = self.df_dict.to_dict("records")
                locations_insert = locations_table.insert().values(df_dict)
                conn.execute(locations_insert)
                print("locations data inserted successfully.")
        except SQLAlchemyError as err:
            print(f"[Full Error]: {str(err)}")
            print(f"Error dumping {self.file_path}")
        finally:
            self.engine.dispose()
