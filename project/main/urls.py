from django.urls import path
from . import views
urlpatterns = [
    path("currencies/", views.CurrenciesView.as_view(), name="currencies"),
    path("currencies/<int:pk>/", views.CurrencyView.as_view(), name="currencies"),
]
