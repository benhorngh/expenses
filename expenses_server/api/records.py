from typing import Optional, List

from fastapi import APIRouter

from expenses_server.common.models import RecordsRequest, AggregateBy, SortBy, RecordsResponseModel, Include, \
    RecordsUpdate, ChangeCategoryRequest
from expenses_server.services import records_service, categorize_service

records_router = APIRouter(prefix="/records", tags=['records'])


@records_router.get("", response_model=RecordsResponseModel)
async def get_all_records(aggregate: Optional[AggregateBy] = None,
                          sort_by: Optional[SortBy] = SortBy.DATE,
                          include: Optional[Include] = Include.ALL,
                          desc: Optional[bool] = False):
    return records_service.get_records(RecordsRequest(aggregate=aggregate, sort_by=sort_by, include=include, desc=desc))


@records_router.patch("")
async def change_category(update: ChangeCategoryRequest):
    if update.transactions_ids:
        for transaction_id in update.transactions_ids:
            categorize_service.categorize_by_transaction_id(update.record.category, transaction_id)
    elif update.businesses:
        for business_name in update.businesses:
            categorize_service.categorize_by_business_name(update.record.category, business_name)
    else:
        raise ValueError("Missing info")
