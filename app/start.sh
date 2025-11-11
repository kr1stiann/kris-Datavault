#!/bin/bash
set -e

echo "⏳ Waiting for Postgres to be ready..."
until pg_isready -h db -U $POSTGRES_USER -d $POSTGRES_DB > /dev/null 2>&1; do
  sleep 1
done

echo "Postgres is ready, running Alembic migrations..."
alembic upgrade head || true

echo "Seeding database..."
python - <<'EOF'
from app.seed import seed_data
from app.app import app
from app.models import db

with app.app_context():
    seed_data()
EOF


echo "🚀 Starting Flask app..."
flask --app app/app.py run --host=0.0.0.0 --port=${PORT:-5001}

