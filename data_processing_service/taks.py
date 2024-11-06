from celery import shared_task
from .models import UploadedFile
import pandas as pd

@shared_task
def process_file(file_id):
    file = UploadedFile.objects.get(id=file_id)
    df = pd.read_csv(file.file.path)
    # Process data (clean, transform, etc.)
    # Insert data in batches
    for i in range(0, len(df), 1000):
        batch_data = df[i:i+1000]
        # Insert batch_data into the database
