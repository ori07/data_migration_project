from django.urls import path
from . import views

urlpatterns = [
    path("process_file/", views.DataProcessingView.as_view()),
]