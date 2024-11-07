import requests
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FileUploadSerializer


class FileUploadView (APIView):

    def post(self, request):
        serializer = FileUploadSerializer(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            uploaded_file = validated_data['file']
            table_name = validated_data['table_name']
            # Save the file to a temporary directory
            fs = FileSystemStorage(location='tmp')
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)

            # Wrapping the data to process
            data_to_send = {
                'filepath': file_url,
                'table_name': table_name
            }
            headers = {'Content-Type': uploaded_file.content_type}
            print("llamando al metodo process_file, del servicio data_processing_service")
            response = requests.post('http://127.0.0.1:8000/data_processing_service/process_file', json=data_to_send, headers=headers)
            if response.status_code == 200:
                print('Archivo procesado, Saliendo del metodo POST en views')
                return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Data processing failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)