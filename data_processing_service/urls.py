from django.urls import path
from .views import DataProcessingView

urlpatterns = [
    path("process_file/", DataProcessingView.as_view(), name='process_view'),
]