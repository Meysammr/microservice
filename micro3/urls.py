from django.urls import path
from .views import FormulaCalculation

urlpatterns = [
    path('calculate-formula/', FormulaCalculation.as_view(), name='calculate_formula'),
]