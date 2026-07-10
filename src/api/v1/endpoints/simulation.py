from fastapi import APIRouter, HTTPException

from src.api.deps import RedisDep, SessionDep
from src.schemas.simulation import (
    SimulationCreate,
    SimulationResponse,
)

router = APIRouter()


@router.post("/simulations", response_model=SimulationResponse, status_code=201)
async def create_simulation(
    payload: SimulationCreate,
    db: SessionDep,
    redis: RedisDep,
):
    """Trigger a new business consciousness simulation cycle (parallel universe)."""
    # Placeholder: In the future, this will insert into Postgres, trigger Celery task, and log state.
    return {
        "id": "sim_1234567890",
        "name": payload.name,
        "status": "pending",
        "parameters": payload.parameters,
        "created_at": "2026-07-10T13:00:00Z",
    }


@router.get("/simulations/{simulation_id}", response_model=SimulationResponse)
async def get_simulation(
    simulation_id: str,
    db: SessionDep,
):
    """Retrieve the status and results of a specific simulation."""
    # Placeholder: In the future, this will fetch from Postgres.
    if simulation_id != "sim_1234567890":
        raise HTTPException(status_code=404, detail="Simulation not found")

    return {
        "id": simulation_id,
        "name": "Sample Simulation",
        "status": "completed",
        "parameters": {"test": "value"},
        "created_at": "2026-07-10T13:00:00Z",
    }
