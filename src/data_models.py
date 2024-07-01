from sqlalchemy import Column, Integer, String, Date, Float, UniqueConstraint
from sqlalchemy.orm import declarative_base
from create_session import engine  # SQLAlchemy engine imported from 'create_session.py'

Base = declarative_base()


class WeatherRecord(Base):
    """ SQLAlchemy model for weather records """

    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True)
    station_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    max_temp = Column(Float)
    min_temp = Column(Float)
    precipitation = Column(Float)

    # Ensures that combination of station_id and date is unique
    __table_args__ = (UniqueConstraint('station_id', 'date', name='uix_station_date'),)


class WeatherStats(Base):
    """ SQLAlchemy model for weather statistics """

    __tablename__ = 'weather_stats'

    id = Column(Integer, primary_key=True)
    station_id = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    avg_max_temp = Column(Float)
    avg_min_temp = Column(Float)
    total_precipitation = Column(Float)


# Create all tables in the engine's database
Base.metadata.create_all(engine)
