from celery import Celery

from src.core.config import settings

# Instantiate Celery
celery_app = Celery(
    "omniverse_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

# Production-grade worker configurations
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,  # 1 hour timeout limit
)

# Auto-discover tasks within our workers packages
celery_app.autodiscover_tasks(["src"])
