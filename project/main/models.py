from .constants import CurrencyType
from project.common.models import Base

from django.db import models


class Currency(Base):
    currency_type = models.PositiveIntegerField(
        choices=CurrencyType.choices,
        null=True,
        blank=True,
    )
    amount = models.FloatField(blank=False, null=False, default=0)
