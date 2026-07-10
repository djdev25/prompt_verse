from datetime import datetime
from typing import Any, Dict
from pydantic import BaseModel, Field


class SimulationBase(BaseModel):
    name: str = Field(..., examples=["Q3 Market Disruptor Simulation"])
    parameters: Dict[str, Any] = Field(
        default_factory=dict,
        examples=[{"risk_tolerance": "high", "agent_count": 5}],
    )


class SimulationCreate(SimulationBase):
    pass


class SimulationResponse(BaseModel):
    id: str
    name: str
    status: str = Field(..., examples=["pending", "running", "completed", "failed"])
    parameters: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True
