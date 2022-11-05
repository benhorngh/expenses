import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from expenses_server.api.records import records_router
from expenses_server.common import settings, utils
from expenses_server.api.statistics import statistics_router
from expenses_server.database.dummy_db import DummyDB

app = FastAPI()


def init_settings():
    settings.init_settings(db_instance=DummyDB())


def init_data():
    utils.init_db()


def init_api():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(statistics_router, prefix='/api/v1')
    app.include_router(records_router, prefix='/api/v1')


if __name__ == "__main__":
    init_settings()
    init_data()
    init_api()
    uvicorn.run(app, host='localhost')
