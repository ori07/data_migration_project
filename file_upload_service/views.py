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
            fs = FileSystemStorage(location='data_processing_service/tmp')
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)

            # Wrapping the data to process
            data_to_send = {
                'file_path': file_url,
                'table_name': table_name
            }
            #headers = {'Content-Type': uploaded_file.content_type}
            print("llamando al metodo process_file, del servicio data_processing_service")
            # Construct absolute URL
            # url = request.build_absolute_uri(reverse('process_view'))
            url = 'http://localhost:8000/process_file/'
            #url = reverse('process_view')
            print(url)
            response = requests.post(url, json=data_to_send)
            if response.status_code == 200:
                print('Archivo procesado, Saliendo del metodo POST en views')
                return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Data processing failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)