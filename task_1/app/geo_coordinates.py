import requests
from typing import Tuple, Any

from .logger import logger


class GeoCoordinates:
    @classmethod
    def get_coordinates(cls, city_name: str) -> Tuple[Any]:
        try:
            url = "https://nominatim.openstreetmap.org/search"
            params = {
                "q": city_name,
                "format": "json",
                "limit": 1
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if len(data) > 0:
                latitude = data[0]["lat"]
                longitude = data[0]["lon"]
                logger.info(f"Координаты города {city_name}: широта {latitude}, долгота {longitude}")
                return float(latitude), float(longitude)
            else:
                logger.warning(f"Город {city_name} не найден.")
                return None
        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе к Nominatim API: {e}")
            return None