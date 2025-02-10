from .models import Currency
from .serializers import CurrencySerializer
from rest_framework import generics, status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CurrenciesView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CurrencyView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)