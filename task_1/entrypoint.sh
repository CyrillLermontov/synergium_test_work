#!/bin/sh

if alembic history | grep "No migrations present"; then
  echo "Нет миграций. Создаем начальную миграцию..."
  alembic revision --autogenerate -m "Initial migration"
  echo "Применяем миграции..."
  alembic upgrade head
else
  echo "Миграции найдены. Применяем миграции..."
  alembic upgrade head
fi

echo "Запуск приложения..."
exec python -m app.main
