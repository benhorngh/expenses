from fastapi import FastAPI

from expenses_server.common import settings, utils
from expenses_server.database.dummy_db import DummyDB
from expenses_server.services import statistics_service
from expenses_server.common.settings import AppSettings

app = FastAPI()


def init_settings():
    settings.init_settings(db_instance=DummyDB())


def init_data():
    utils.init_db()


if __name__ == "__main__":
    init_settings()
    init_data()

    data = AppSettings.settings.db_instance.get_all_transaction()
    print(statistics_service.get_statistics())
