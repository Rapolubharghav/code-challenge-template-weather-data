from sqlalchemy import func
from datetime import datetime
import logging
from create_session import Session  # SQLAlchemy's session creation imported from 'create_session.py'
from data_models import WeatherRecord, WeatherStats  # SQLAlchemy models imported from 'data_models.py'


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_weather_stats():
    """
    Calculate and store weather statistics per station and year.

    This function queries weather records from the database,
    calculates statistics, and stores them in the WeatherStats table.
    """
    start_time = datetime.now()
    logger.info(f'Starting statistics calculation at {start_time}')

    # Use context management for session
    with Session() as session:
        # Query to calculate weather statistics using SQLAlchemy's func methods
        records = session.query(
            WeatherRecord.station_id,
            func.extract('year', WeatherRecord.date).label('year'),
            func.avg(WeatherRecord.max_temp).label('avg_max_temp'),
            func.avg(WeatherRecord.min_temp).label('avg_min_temp'),
            func.sum(WeatherRecord.precipitation).label('total_precipitation')
        ).group_by(
            WeatherRecord.station_id,
            func.extract('year', WeatherRecord.date)
        ).all()

        # Iterate through query results and populate WeatherStats table
        for record in records:
            stat = WeatherStats(
                station_id=record.station_id,
                year=int(record.year),
                avg_max_temp=record.avg_max_temp,
                avg_min_temp=record.avg_min_temp,
                total_precipitation=record.total_precipitation
            )
            session.add(stat)

        # Commit changes to the database inside the context manager
        session.commit()

    end_time = datetime.now()
    logger.info(f'Finished statistics calculation at {end_time}, duration: {end_time - start_time}')


# Call the function to calculate and store weather statistics
calculate_weather_stats()
