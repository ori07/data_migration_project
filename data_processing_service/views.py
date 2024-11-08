import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from file_upload_service.models import Job, Department, Hired_Employee, UploadedFile

class DataProcessingView (APIView):

    def post(self, request):
        print("Entrando a Process File")
        data = request.data
        file_path = data['file_path']
        table_name = data['table_name']
        file_path = os.path.join(settings.BASE_DIR, 'data_processing_service/tmp/job_data_test.csv')
        df = pd.read_csv(file_path, header=None)
        df = df.reset_index()
        df.columns = ['index','id', 'job']
        # Assign the corresponding model
        if table_name == 'Job':
            model = Job
            objects = [Job(id=row['id'], job=row['job']) for index, row in df.iterrows()]

        elif table_name == 'Department':
            model = Department
        elif table_name == 'Hired_employee':
            model = Hired_Employee

        # Insert data in batches
        print("insert into database")
        model.objects.bulk_create(objects)
        # Process data (clean, transform, etc.)
        # Delete the temporary file
        os.remove(file_path)
        return Response({'message': 'Data processed successfully'})




