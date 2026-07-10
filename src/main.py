from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.api import api_router
from src.core.config import settings
from src.core.redis import redis_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    # App startup logic
    yield
    # App shutdown logic - clean closing of Redis connection pool
    await redis_pool.disconnect()


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="OmniVerse AI: The Business Consciousness Engine",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS Middleware
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Mount API routers
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Root redirect / introduction."""
    return {
        "message": f"Welcome to the {settings.PROJECT_NAME} Engine",
        "docs": "/docs",
        "healthcheck": f"{settings.API_V1_STR}/health",
    }
