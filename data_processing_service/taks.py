from celery import shared_task
from .models import Job, Department, Hired_Employee, UploadedFile
import pandas as pd

@shared_task
def process_file(file_id, table_name):
    file = UploadedFile.objects.get(id=file_id)
    df = pd.read_csv(file.file.path)
    if table_name == 'Job':
        model = Job
    elif table_name =='Department':
        model = Department
    elif table_name == 'Hired_employee':
        model = Hired_Employee

    # Insert data in batches
    model.objects.bulk_create(objects)
    # Process data (clean, transform, etc.)




