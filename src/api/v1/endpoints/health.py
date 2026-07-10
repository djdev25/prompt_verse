from fastapi import APIRouter
from sqlalchemy import text

from src.api.deps import RedisDep, SessionDep

router = APIRouter()


@router.get("/health", status_code=200)
async def health_check(db: SessionDep, redis: RedisDep):
    """Verify that the FastAPI instance, PostgreSQL, and Redis are reachable."""
    # Test PostgreSQL Connection
    try:
        await db.execute(text("SELECT 1"))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    # Test Redis Connection
    try:
        await redis.ping()
        redis_status = "healthy"
    except Exception as e:
        redis_status = f"unhealthy: {str(e)}"

    return {
        "status": "online",
        "services": {
            "database": db_status,
            "redis": redis_status,
        },
    }
