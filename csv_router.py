"""
process and return csv data
"""
from fastapi import APIRouter
from schemas import StatsInfo

router = APIRouter()


@router.get("/csv")
async def csv_data():
    """
    return csv data
    """
    return {"pullups": "csv data",
            "meters": "csv data"}


@router.post("/csv")
async def csv_data(stats: StatsInfo):
    """
    return csv data
    """
    print(stats.meters, stats.pullups)
    return {"pullups": stats.pullups,
            "meters": stats.meters}
