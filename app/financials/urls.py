from django.urls import path
from .views import (
    Financials
)


urlpatterns = [
    path('financials/<financial_statement>/', Financials.as_view(),name='financials'),
]
