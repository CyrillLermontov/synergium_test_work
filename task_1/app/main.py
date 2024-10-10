import asyncio

from .weather_data_dao import WeatherDataDAO
from .geo_coordinates import GeoCoordinates
from .weather_api import WeatherAPIClient
from .config import WEATHER_API_URL, CITY, TODAY, TWO_MONTHS_AGO


async def main():
    coords = GeoCoordinates.get_coordinates(city_name=CITY)
    api_client = WeatherAPIClient(base_url=WEATHER_API_URL, latitude=coords[0], longitude=coords[1])
    weather_data = api_client.get_historical_weather(
        start_date=TWO_MONTHS_AGO.strftime("%Y-%m-%d"),
        end_date=TODAY.strftime("%Y-%m-%d")
    )
    await WeatherDataDAO.add_data(weather_data)
    await WeatherDataDAO.calculate_statistics()


if __name__ == "__main__":
    asyncio.run(main())
