# models for end points
from pydantic import BaseModel


class StatsInfo(BaseModel):
    pullups: int
    meters: int
