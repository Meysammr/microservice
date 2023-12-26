from django.urls import path
from .views import AggregationView

urlpatterns = [
    path('aggregation/', AggregationView.as_view(), name='aggregation-view'),
]