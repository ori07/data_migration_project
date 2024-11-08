from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from .models import UploadedFile




import logging
logger = logging.getLogger(__name__)

# Define test for upload simple record for the three tables of the model
class UploadFileTest(TestCase):
    def test_upload_file(self):
        client = APIClient()
        # Create a sample CSV file
        csv_file_1 = SimpleUploadedFile('job_data_test.csv', b"1,Job1")
        csv_file_2 = SimpleUploadedFile('department_data_test.csv', b"1,Department1")
        csv_file_3 = SimpleUploadedFile('hired_employees_test.csv', b"1,John Doe,2021-04-23T23:45:42Z,1,1")

        # Upload the files
        # Job file
        print(reverse('upload_view'))
        response = self.client.post(reverse('upload_view'), {'file': csv_file_1, 'table_name':'Job'})
        print(response)
        assert response.status_code == 201
        #uploaded_file = UploadedFile.objects.last()
        #assert uploaded_file is not None



        # Department file -- TODO
        #response = client.post('/upload/', {'file': csv_file_2})
        #assert response.status_code == 201
        #uploaded_file = UploadedFile.objects.last()
        #assert uploaded_file is not None

        # Hired_employee file
        #response = client.post('/upload/', {'file': csv_file_3})
        #assert response.status_code == 201
        #uploaded_file = UploadedFile.objects.last()
        #assert uploaded_file is not None
