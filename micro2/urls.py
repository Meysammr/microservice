from django.urls import path

from .views import create_aggregations

urlpatterns = [
    path('create-aggregations/', create_aggregations, name='create_aggregations')
]