from django.urls import path, include
from . import views

urlpatterns = [
    path("upload/", views.FileUploadView.as_view(), name='upload_view'),
]
