from datetime import datetime

import requests


class MoneyLover:
    WALLETS_LIST = {}
    CATEGORIES_LIST = {}
    AUTHORIZATION_TOKEN = None

    @staticmethod
    def init_data(authorization_token):
        MoneyLover.AUTHORIZATION_TOKEN = authorization_token
        MoneyLover.WALLETS_LIST = MoneyLover._get_wallets()
        MoneyLover.CATEGORIES_LIST = MoneyLover._get_categories()

    @staticmethod
    def _get_wallets():
        assert MoneyLover.AUTHORIZATION_TOKEN, 'MONEY LOVER authorization token missing'
        res = requests.post('https://web.moneylover.me/api/wallet/list',
                            headers={'Authorization': MoneyLover.AUTHORIZATION_TOKEN,
                                     'Content-Type': 'application/json; charset=utf-8'})
        assert res.status_code == 200
        assert res.json()['error'] == 0, res.text
        return res.json()

    @staticmethod
    def _get_categories():
        res = requests.post('https://web.moneylover.me/api/category/list-all',
                            headers={'Authorization': MoneyLover.AUTHORIZATION_TOKEN,
                                     'Content-Type': 'application/json; charset=utf-8'})
        assert res.status_code == 200
        assert res.json()['error'] == 0, res.text
        return res.json()

    @staticmethod
    def add_to_wallet(account_id, transaction_date: datetime, amount, category_id, note):
        t_date = f'{transaction_date.year}-{str(transaction_date.month).zfill(2)}-{str(transaction_date.day).zfill(2)}'
        t_note = note.replace('"', '') if note else ''
        body = f'"with": [], "account": "{account_id}", "category": "{category_id}", "amount": {amount}, "note": "{t_note}" , "displayDate": "{t_date}", "event": "", "exclude_report": false, "longtitude": 0, "latitude": 0, "addressName": "", "addressDetails": "", "addressIcon": "", "image": ""'
        body = '{' + body + '}'
        res = requests.post('https://web.moneylover.me/api/transaction/add', data=body.encode('utf-8'),
                            headers={'Authorization': MoneyLover.AUTHORIZATION_TOKEN,
                                     'Content-Type': 'application/json; charset=utf-8'})
        assert res.status_code == 200
        assert res.json()['error'] == 0, res.text

    @staticmethod
    def get_category_id_by_name(name: str, wallet_id: str):
        return \
            [c for c in MoneyLover.CATEGORIES_LIST['data'] if
             name.lower() in c['name'].lower() and c['account'] == wallet_id][
                0][
                '_id']

    @staticmethod
    def get_wallet_id_by_name(wallet_name: str):
        return [w for w in MoneyLover.WALLETS_LIST['data'] if w['name'].lower() == wallet_name.lower()][0]['_id']
