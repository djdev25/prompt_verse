FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry to install dependencies system-wide
RUN poetry config virtualenvs.create false \
    && if [ -f poetry.lock ]; then poetry install --no-interaction --no-ansi; else poetry install --no-interaction --no-ansi --no-root; fi

# Copy project files
COPY . /app

CMD ["celery", "-A", "src.core.celery_app", "worker", "--loglevel=info"]
