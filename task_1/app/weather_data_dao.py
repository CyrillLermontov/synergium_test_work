from typing import Union, Dict, List, Any
from datetime import datetime

from .database import async_session_maker
from .models import WeatherData
from .logger import logger

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, desc, select


class WeatherDataDAO:
    @classmethod
    async def add_data(cls, data: Union[Dict[str, Any], List[Any]]) -> None:
        try:
            async with async_session_maker() as session:
                daily_data = data["daily"]
                time_data = daily_data["time"]
                for i in range(len(time_data)):
                    new_data = WeatherData(
                        date=datetime.strptime(daily_data["time"][i], '%Y-%m-%d').date(),
                        max_temperature=daily_data["temperature_2m_max"][i],
                        min_temperature=daily_data["temperature_2m_min"][i],
                        max_feels_like_temperature=daily_data["apparent_temperature_max"][i],
                        min_feels_like_temperature=daily_data["apparent_temperature_min"][i],
                        weather_code=daily_data["weathercode"][i],
                        max_wind_speed=daily_data["windspeed_10m_max"][i]
                    )
                    session.add(new_data)
                await session.commit()
                logger.info("Данные погоды успешно добавлены в базу данных.")
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при добавлении данных в базу данных: {e}")
            await session.rollback() 
        except Exception as e:
            logger.error(f"Неизвестная ошибка: {e}")

    @classmethod
    async def calculate_statistics(cls) -> None:
        try:
            async with async_session_maker() as session:
                    sunny_days_count_query = select(func.count()).where(WeatherData.weather_code.in_([0, 1]))
                    sunny_days_count_result = await session.execute(sunny_days_count_query)
                    sunny_days_count = sunny_days_count_result.scalar()

                    hot_days_count_query = select(func.count()).where(WeatherData.max_temperature > 20)
                    hot_days_count_result = await session.execute(hot_days_count_query)
                    hot_days_count = hot_days_count_result.scalar()

                    top_days_query = select(WeatherData).order_by(
                        desc(WeatherData.max_temperature),
                        desc(WeatherData.max_wind_speed)
                    ).limit(3)
                    top_days_result = await session.execute(top_days_query)
                    top_days_list = top_days_result.fetchall()
                    logger.info(f"Количество солнечных дней: {sunny_days_count}")
                    logger.info(f"Количество дней с температурой выше 20°C: {hot_days_count}")
                    logger.info(f"Топ-3 дня с самой высокой температурой и самой сильной скоростью ветра:")
                    for day in top_days_list:
                        logger.info(f"Дата: {day[0].date}, Температура: {day[0].max_temperature}, Скорость ветра: {day[0].max_wind_speed}")
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при запросе к базе: {e}")
            await session.rollback() 
        except Exception as e:
            logger.error(f"Ошибка при вычислении статистики: {e}")
