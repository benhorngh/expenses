from datetime import date


def single_transaction(business: str, t_date: date) -> str:
    t_date_str = t_date.strftime('%d/%m/%Y')
    return f'In {business.strip()}, \n at {t_date_str}'


def business_visits(business: str, times: int) -> str:
    return f'In {business.strip()}, \n {times} visits'
