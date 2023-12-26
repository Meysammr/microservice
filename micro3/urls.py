from django.urls import path
from .views import FormulaCalculation

urlpatterns = [
    path('calculate/', FormulaCalculation.as_view(), name='calculate_formula'),
]
