from django.urls import path, include
from . import views

urlpatterns = [
    path("upload/", views.FileUploadView.as_view(), name='upload_view'),
    # path('', include(file_upload_service.urls, namespace='file_upload')),

]
