from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .tasks import process_file
from file_upload_service.models import Job, Department, Hired_Employee, UploadedFile

class DataProcessingTestCase(TestCase):

    # Define test for read and save the data into database
    def test_data_processing(self):
        # Create a test UploadedFile instance
        uploaded_file = UploadedFile.objects.create(file=SimpleUploadedFile('test_data_job.csv', b"1,Job1"))
        # Trigger the data processing task: Test insert to Job table
        process_file(uploaded_file.id, 'Job')
        #Check if data is inserted into the database
        assert Job.objects.count() == 1

        # Create a test UploadedFile instance
        uploaded_file = UploadedFile.objects.create(file=SimpleUploadedFile('test_data_dep.csv', b"1,Department1"))
        # Trigger the data processing task: Test insert to Department table
        process_file(uploaded_file.id, 'Department')
        assert Department.objects.count() == 1

        # Test uploading to Hired_Employee table
        # Create Job and Department instances first
        Job.objects.create(job="Job2")
        Department.objects.create(department="Department2")

        # Create a test UploadedFile instance
        uploaded_file = UploadedFile.objects.create(file=SimpleUploadedFile('test_data_dep.csv', b"1,John Doe,2021-04-23T23:45:42Z,2,2"))
        # Trigger the data processing task: Test insert to Hired_Employee table
        process_file(uploaded_file.id, 'Hired_Employee')
        assert Hired_Employee.objects.count() == 1
