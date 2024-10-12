


from datetime import datetime, timedelta
<<<<<<< HEAD
from .deposite_schema import DepositSchema
=======

from app.deposite.deposite_schema import DepositSchema

>>>>>>> 25c9873 ( On branch developer)
from ..main import DATE_FORMAT


def calculate_deposit(schema: DepositSchema) -> dict[str, float]:
    start_date: datetime = datetime.strptime(schema.date, DATE_FORMAT)

    monthly_rate: float = schema.rate / 100 / 12

    results: dict[str, float] = {}

    current_amount: float = schema.amount
    for period in range(schema.periods):

        interest: float = current_amount * monthly_rate
        current_amount += interest


        next_date = start_date + timedelta(days=30 * (period + 1))

        formatted_date = next_date.strftime(DATE_FORMAT)

        results[formatted_date] = round(current_amount, 2)
        # results[f'{next_date:%d.%m.%Y}'] = round(current_amount, 2)

    return results
