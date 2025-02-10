import requests
from .models import Currency
from .constants import CurrencyType
from celery import shared_task

@shared_task
def get_currencies():
    response = requests.get('https://api.frankfurter.dev/v1/latest')
    if response.status_code == 200:
        rates = response.json().get('rates', {})
        for currency in CurrencyType:
            currency_code = currency.name
            if currency_code in rates:
                amount = rates[currency_code]
                Currency.objects.update_or_create(
                    currency_type=currency.value,
                    defaults={'amount': amount}
                )