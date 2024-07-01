from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy engine that connects to the SQLite database 'weather_data.db'
engine = create_engine('sqlite:///weather_data.db')

# Create a sessionmaker that will manage the database connections
Session = sessionmaker(bind=engine)

# The Session class created here is a factory for creating new Session objects bound to this engine.
# When a new Session object is instantiated, it will be bound to the SQLite database 'weather_data.db'.