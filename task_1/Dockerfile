FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

COPY alembic.ini alembic.ini
COPY ./migrations ./migrations

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh  # Делаем скрипт исполняемым

ENTRYPOINT ["/entrypoint.sh"]
