from typing import Optional

from fastapi import APIRouter

from expenses_server.common.models import RecordsRequest, AggregateBy, SortBy, RecordsResponseModel, Include
from expenses_server.services import records_service

records_router = APIRouter(prefix="/records", tags=['records'])


@records_router.get("", response_model=RecordsResponseModel)
async def get_all_records(aggregate: Optional[AggregateBy] = None,
                          sort_by: Optional[SortBy] = SortBy.DATE,
                          include: Optional[Include] = Include.ALL,
                          desc: Optional[bool] = False):
    return records_service.get_records(RecordsRequest(aggregate=aggregate, sort_by=sort_by, include=include, desc=desc))
