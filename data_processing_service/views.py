import os
import pandas as pd
from rest_framework.views import APIView
from file_upload_service.models import Job, Department, Hired_Employee, UploadedFile

class DataProcessingView (APIView):
    def process_file(request):
        print("Entrando a Process File")
        data = request.data
        file_path = data['file_path']
        table_name = data['table_name']
        print(file_path)
        print(table_name)
        df = pd.read_csv(file.path)

        # Assign the corresponding model
        if table_name == 'Job':
            print("Model Job assigned")
            model = Job
        elif table_name =='Department':
            model = Department
        elif table_name == 'Hired_employee':
            model = Hired_Employee

        # Insert data in batches
        model.objects.bulk_create(objects)
        # Process data (clean, transform, etc.)
        # Delete the temporary file
        os.remove(file_path)




