FROM python:3.11-slim

# Systempaket för psycopg2 + Postgres client tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera källkod
COPY app ./app

ENV PYTHONUNBUFFERED=1
EXPOSE 5001

CMD ["./app/start.sh"]
