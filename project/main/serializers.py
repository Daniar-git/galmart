from rest_framework import serializers
from .models import Currency
from .constants import CurrencyType


class CurrencySerializer(serializers.ModelSerializer):
    currency_type = serializers.SerializerMethodField()

    def get_currency_type(self, obj):
        return CurrencyType(obj.currency_type).label

    class Meta:
        model = Currency
        fields = '__all__'