FROM python:3.11-slim

# Systempaket för psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Installera Python-beroenden först (bättre caching)
COPY app/requirements.txt ./app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Kopiera källkod
COPY app ./app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000
