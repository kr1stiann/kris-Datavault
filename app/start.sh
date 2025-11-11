#!/bin/bash
set -e

echo "Waiting for Postgres to be ready..."

RETRIES=30
until psql "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:5432/${POSTGRES_DB}" -c '\q' 2>/dev/null || [ $RETRIES -eq 0 ]; do
  echo "Postgres not ready yet... (${RETRIES} retries left)"
  RETRIES=$((RETRIES-1))
  sleep 2
done

echo "Postgres is ready, running Alembic migrations..."
flask db upgrade || true

echo "Seeding database..."
python -c "from app.seed import seed_data; seed_data()"

PORT=${PORT:-5001}
echo "Starting Flask with Gunicorn on 0.0.0.0:${PORT} ..."
exec gunicorn -b 0.0.0.0:${PORT} app:app
