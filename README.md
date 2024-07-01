# Weather Data API

This project is a Django REST API for weather data, which includes ingestion, statistical analysis, and data representation through API endpoints.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Data Model Setup](#data-model-setup)
- [Data Ingestion](#data-ingestion)
- [Data Analysis](#data-analysis)
- [Running the API](#running-the-api)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)

## Requirements
- Python 3.8+
- Django 3.2+
- Django REST framework
- SQLite
- pip (Python package installer)

## Installation
1. **Clone the repository**
   
   ```sh
   git clone https://github.com/Rapolubharghav/code-challenge-template-weather-data.git
   cd code-challenge-template-weather-data
   
2. **Install Dependencies**
   
   Install Python dependencies using pip. It's recommended to use a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

## Data Model Setup
1. **Create Database Session**
   
   Run create_session.py to initialize the database session:
   ```sh
   python create_session.py

2. **Create Database Tables**
   
   Execute data_models.py to create tables (weather_records and weather_stats) in SQLite:
   ```sh
   python data_models.py

## Data Ingestion

**Ingest Data**
   
   Use data_ingestion.py to ingest weather data into weather_records:
   
   ```sh
   python data_ingestion.py
   ```

## Data Analysis

**Perform Statistical Analysis**
   
   Run the statistical analysis script statistical_analysis_weather_data.py to calculate weather statistics based on the ingested data:
   ```sh
   python statistical_analysis_weather_data.py
   ```
## Running the API

1. **Setting up the Django Project**

   Navigate to the weather_api directory and make migrations for the app.
   
   ```sh
   cd weather_api
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Running the Development Server**

   Start the Django development server.
   
   ```sh
   python manage.py runserver
   ```
## Testing

   To run the tests, use the following command:
   
   ```sh
   python manage.py test
   ```
   
## API Endpoints

Weather Records: http://127.0.0.1:8000/api/weather/

Weather Stats: http://127.0.0.1:8000/api/weather/stats/

Swagger UI: http://127.0.0.1:8000/swagger/ (Automatic documentation)
