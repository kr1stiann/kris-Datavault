FROM python:3.11-slim

# System packages for psycopg2 + Postgres client
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app ./app

# Environment setup
ENV PYTHONUNBUFFERED=1
EXPOSE 5001

CMD ["bash", "./app/start.sh"]
