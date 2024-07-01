import os
import logging
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from create_session import Session
from data_models import WeatherRecord

# Setup logging configurations
logging.basicConfig(
    filename='data_ingestion.log', #log file name
    level=logging.INFO, #Log level
    format='%(asctime)s - %(levelname)s - %(message)s' #Log message Format
)

script_dir = os.path.dirname(os.path.abspath(__file__))
# Define path to directory containing weather data
WX_DATA_PATH = os.path.join(script_dir,'..','wx_data')

def ingest_weather_data(file_path, session):
    start_time = datetime.now() #Record the start time of the ingestion process
    logging.info(f'Starting ingestion for file: {os.path.basename(file_path)} at {start_time}')
    print(f'Starting ingestion for file: {os.path.basename(file_path)} at {start_time}')
    records_to_insert = [] #list to hold records to be inserted
    records_ingested = 0 # counter for records ingested
    duplicate_records = 0 # COunter for duplicate records

    with open(file_path, 'r') as file:
        station_id = os.path.basename(file_path).split('.')[0]  # Extract station ID from file name
        for line in file:
            date_str, max_temp, min_temp, precipitation = line.strip().split('\t')
            date = datetime.strptime(date_str, '%Y%m%d').date() # Convert date string to date object

            if max_temp == '-9999':
                max_temp = None
            else:
                max_temp = int(max_temp) / 10.0

            if min_temp == '-9999':
                min_temp = None
            else:
                min_temp = int(min_temp) / 10.0

            if precipitation == '-9999':
                precipitation = None
            else:
                precipitation = int(precipitation) / 10.0

            record = WeatherRecord(
                station_id=station_id,
                date=date,
                max_temp=max_temp,
                min_temp=min_temp,
                precipitation=precipitation
            )

            records_to_insert.append(record)

    try:
        session.bulk_save_objects(records_to_insert)
        session.commit() # Commit the transaction
        records_ingested = len(records_to_insert)  # Update the count of records ingested
    except IntegrityError:
        # Handle the case where bulk insert fails due to duplicates
        session.rollback()  # Roll back the transaction
        for record in records_to_insert:
            try:
                session.add(record) # Try to add each record individually
                session.commit()  # Commit the transaction
                records_ingested += 1 # Update the count of records ingested
            except IntegrityError:
                session.rollback()  # Roll back the transaction
                duplicate_records += 1 # Update the count of duplicate records

    end_time = datetime.now()
    logging.info(f'File: {file_path}')
    logging.info(f'Start Time: {start_time}')
    logging.info(f'End Time: {end_time}')
    logging.info(f'Records Ingested: {records_ingested}')
    logging.info(f'Duplicate Records: {duplicate_records}')

    print(f"End Time: {end_time}")
    print(f"Records Ingested: {records_ingested}")
    print(f"Duplicate Records: {duplicate_records}")

    return records_ingested, duplicate_records

def main():
    # Connect to the database
    session = Session()

    total_records_ingested = 0
    total_duplicate_records = 0
    main_start_time = datetime.now()

    # Ingest all files in the specified directory
    for root, dirs, files in os.walk(WX_DATA_PATH):
        for file in files:
            file_path = os.path.join(root, file) # Get the full path of the file
            records_ingested, duplicate_records = ingest_weather_data(file_path, session)
            # Update totals
            total_records_ingested += records_ingested
            total_duplicate_records += duplicate_records

    main_end_time = datetime.now() # Record the end time of the main ingestion process
    total_time = main_end_time - main_start_time # Calculate the total time taken
    # Log the summary of the ingestion process
    logging.info(f'Total Ingestion Start Time: {main_start_time}')
    logging.info(f'Total Ingestion End Time: {main_end_time}')
    logging.info(f'Total Time: {total_time}')
    logging.info(f'Total Records Ingested: {total_records_ingested}')
    logging.info(f'Total Duplicate Records: {total_duplicate_records}')
    # Print the summary of the ingestion process
    print(f"Total Ingestion Start Time: {main_start_time}")
    print(f"Total Ingestion End Time: {main_end_time}")
    print(f"Total Time: {total_time}")
    print(f"Total Records Ingested: {total_records_ingested}")
    print(f"Total Duplicate Records: {total_duplicate_records}")

if __name__ == "__main__":
    main()
