from fastapi import APIRouter

from expenses_server.common.models import StatisticsResponseModel
from expenses_server.services import statistics_service

statistics_router = APIRouter(prefix="/statistics", tags=['statistics'])


@statistics_router.get("", response_model=StatisticsResponseModel)
async def get_all_statistics():
    return statistics_service.get_statistics()
