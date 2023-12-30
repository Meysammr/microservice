from django.urls import path
from .views import RawDataAPIView

urlpatterns = [
    path('import-csv/', RawDataAPIView.as_view(), name="Raw_list"),
]