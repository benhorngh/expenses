from expenses_server.common import settings, utils
from expenses_server.services import statistics_service
from expenses_server.common.settings import AppSettings


def init_settings():
    settings.init_settings()


def init_data():
    utils.init_db()


if __name__ == "__main__":
    init_settings()
    init_data()

    data = AppSettings.globals.transaction_db.get_all_data()
    print(statistics_service.get_statistics())
    AppSettings.globals.transaction_db.store_all_data(data)

