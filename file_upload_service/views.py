from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from data_processing_service.taks import process_file
from .serializer import FileUploadSerializer


class FileUploadView (APIView):

    def post(self, request):
        print("Entry to post method")
        print(request.data)
        serializer = FileUploadSerializer(data = request.data)
        print("Validating serializer")
        if serializer.is_valid():
            print('El serializador es valido')
            print(serializer.data['file'])
            print(serializer.data['table_name'])
            process_file.delay(serializer.data['file'], serializer.data['table_name'])
            print('Archivo procesado, Saliendo del metodo POST en views')
            # Store file, send message to data processing service
            return Response({'message':'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)