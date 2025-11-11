#!/bin/bash
set -e

echo "Waiting for Postgres to be ready..."
until pg_isready -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do
  sleep 1
done

echo "Postgres is ready, running Alembic migrations..."
flask db upgrade || true

echo "Seeding database..."
python -c "from app.seed import seed_data; seed_data()"

# Use Render's PORT env var, fallback to 5001 for local
PORT=${PORT:-5001}
echo "🚀 Starting Flask on 0.0.0.0:${PORT} ..."
exec flask --app app.app run --host=0.0.0.0 --port=${PORT}
