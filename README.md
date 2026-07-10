# OmniVerse AI: The Business Consciousness Engine

OmniVerse AI is a high-performance simulation and decision-consciousness platform built for modeling enterprise dynamics across parallel simulation universes.

## Tech Stack
- **Core**: Python 3.11, [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous Web API framework)
- **Database**: PostgreSQL (Structured state schemas and transaction logs) via [SQLAlchemy 2.0](https://www.sqlalchemy.org/) & [asyncpg](https://github.com/MagicStack/asyncpg)
- **Cache & Message Broker**: Redis (Fast shared-state storage and Celery task broker)
- **Asynchronous Task Workers**: [Celery](https://docs.celeryq.dev/) (Distributed background simulation runner)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/) (Async schema versioning)
- **LLM/Structured AI**: OpenAI API and [Instructor](https://github.com/jxnl/instructor)
- **Testing**: [Pytest](https://docs.pytest.org/) & `pytest-asyncio` for comprehensive async endpoint tests

---

## Getting Started Locally

### Prerequisites
- Python 3.11+
- Poetry (Package manager)
- Docker & Docker Compose (optional for local service execution)

### 1. Installation
Clone the repository and install all dependencies:
```bash
poetry install
```

### 2. Configuration
Copy the sample environment variables and customize them:
```bash
cp .env.example .env
```

### 3. Local Orchestration (via Docker Compose)
Launch the API, Worker, Redis, and Postgres services instantly:
```bash
docker-compose up --build
```
The FastAPI web server will start at `http://localhost:8000`. You can access the dynamic interactive API docs at `http://localhost:8000/docs`.

### 4. Running Migrations
Apply Alembic database migrations:
```bash
# Run via local environment
poetry run alembic upgrade head

# Or inside the Docker environment
docker-compose exec web alembic upgrade head
```

### 5. Running the Test Suite
Execute tests with Pytest:
```bash
poetry run pytest
```
