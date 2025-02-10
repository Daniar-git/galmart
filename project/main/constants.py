from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyType(models.IntegerChoices):
    USD = 0, _('USD'),
    CZK = 1, _('CZK'),
