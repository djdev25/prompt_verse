from fastapi import APIRouter

from src.api.v1.endpoints import health, simulation

api_router = APIRouter()

# Include health router (endpoints prefix is handled in path)
api_router.include_router(health.router)
# Include simulation router (prefix can be added here or in the router file)
api_router.include_router(simulation.router)
