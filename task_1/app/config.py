import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)


DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")
CITY = os.getenv("CITY")

TODAY = datetime.today()
TWO_MONTHS_AGO = TODAY - timedelta(days=60)