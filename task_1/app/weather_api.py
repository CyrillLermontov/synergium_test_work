from .logger import logger

import requests
from typing import Union, Dict, List, Any


class WeatherAPIClient:
    def __init__(self, base_url: str, latitude: Union[int, float], longitude: Union[int, float]) -> None:
        self.__base_url = base_url
        self.__latitude = latitude 
        self.__longitude = longitude

    def get_historical_weather(self, start_date: str, end_date: str) -> Union[Union[Dict[str, Any], List[Any]], None]:
        params = {
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "start_date": start_date,
            "end_date": end_date,
            "daily": [
                "temperature_2m_max", 
                "temperature_2m_min", 
                "apparent_temperature_max", 
                "apparent_temperature_min", 
                "weathercode", 
                "windspeed_10m_max"
            ],
            "timezone": "auto"
        }
        try:
            response = requests.get(f"{self.__base_url}/v1/forecast", params=params)
            response.raise_for_status()
            logger.info(f"Данные погоды успешно получены для периода {start_date} - {end_date}.")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе данных погоды: {e}")
            return None
