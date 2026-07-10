import pytest
from httpx import AsyncClient

from src.core.config import settings


@pytest.mark.asyncio
async def test_health_check_endpoint(client: AsyncClient, mock_db, mock_redis):
    """Test that the health check endpoint returns 200 and runs diagnostics."""
    response = await client.get(f"{settings.API_V1_STR}/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "online"
    assert data["services"]["database"] == "healthy"
    assert data["services"]["redis"] == "healthy"

    # Verify mocks were interacted with
    mock_db.execute.assert_called_once()
    mock_redis.ping.assert_called_once()
