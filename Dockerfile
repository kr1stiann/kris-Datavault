# Use a newer, patched base image
FROM python:3.12-slim-bookworm

# Prevents interactive prompts and speeds up apt
ENV DEBIAN_FRONTEND=noninteractive

# Install required system packages for psycopg2 + Postgres client
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Upgrade pip and install dependencies safely
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app ./app

# Create a non-root user (for security)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expose Flask port
EXPOSE 5001

# Start the app
CMD ["./app/start.sh"]
