from redis.asyncio import ConnectionPool, Redis

from src.core.config import settings

# Create an async Redis connection pool
redis_pool = ConnectionPool.from_url(
    settings.REDIS_URL,
    max_connections=50,
    decode_responses=True,
)


def get_redis_client() -> Redis:
    """Get an asynchronous Redis client instance."""
    return Redis(connection_pool=redis_pool)


async def get_redis() -> Redis:
    """Dependency helper for FastAPI endpoints."""
    client = get_redis_client()
    try:
        yield client
    finally:
        await client.close()
