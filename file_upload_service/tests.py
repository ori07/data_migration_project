from django.test import TestCase, Client
from .models import UploadedFile
from django.core.files.uploadedfile import SimpleUploadedFile

import logging
logger = logging.getLogger(__name__)

# Define test for upload simple record for the three tables of the model
class UploadFileTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_upload_file(self):
        # Create a sample CSV file
        csv_file_1 = SimpleUploadedFile('job_data_test.csv', b"1,Job1")
        csv_file_2 = SimpleUploadedFile('department_data_test.csv', b"1,Department1")
        csv_file_3 = SimpleUploadedFile('hired_employees_test.csv', b"1,John Doe,2021-04-23T23:45:42Z,1,1")

        # Upload the files
        # Job file
        response = self.client.post('/upload/', {'file': csv_file_1})
        assert response.status_code == 201
        uploaded_file = UploadedFile.objects.last()
        assert uploaded_file is not None

        # Department file
        response = client.post('/upload/', {'file': csv_file_2})
        assert response.status_code == 201
        uploaded_file = UploadedFile.objects.last()
        assert uploaded_file is not None

        # Hired_employee file
        response = client.post('/upload/', {'file': csv_file_3})
        assert response.status_code == 201
        uploaded_file = UploadedFile.objects.last()
        assert uploaded_file is not None
