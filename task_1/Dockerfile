# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только код приложения в контейнер
COPY ./app ./app

# Копируем alembic.ini и файлы для миграции
COPY alembic.ini alembic.ini
COPY ./migrations ./migrations

# Копируем скрипт для запуска миграций и приложения
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  # Делаем скрипт исполняемым

# Указываем точку входа для запуска контейнера
ENTRYPOINT ["/entrypoint.sh"]
