from sqlalchemy import Column, Integer, Float, Date
from .database import Base


class WeatherData(Base):
    __tablename__ = 'weather_data'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    max_temperature = Column(Float)
    min_temperature = Column(Float)
    max_feels_like_temperature = Column(Float)
    min_feels_like_temperature = Column(Float)
    weather_code = Column(Integer)
    max_wind_speed = Column(Float)

