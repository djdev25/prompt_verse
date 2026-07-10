from unittest.mock import AsyncMock
import pytest
from httpx import ASGITransport, AsyncClient

from src.core.database import get_db
from src.core.redis import get_redis
from src.main import app


@pytest.fixture
def mock_db():
    """Fixture to mock the async database session."""
    session = AsyncMock()
    session.execute.return_value = AsyncMock()
    return session


@pytest.fixture
def mock_redis():
    """Fixture to mock the async Redis client."""
    client = AsyncMock()
    client.ping.return_value = True
    return client


@pytest.fixture
async def client(mock_db, mock_redis):
    """Fixture to provide a test AsyncClient with overridden dependencies."""
    app.dependency_overrides[get_db] = lambda: mock_db
    app.dependency_overrides[get_redis] = lambda: mock_redis

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

    # Clear dependency overrides after test
    app.dependency_overrides.clear()
