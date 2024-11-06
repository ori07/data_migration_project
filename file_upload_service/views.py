from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializer
.serializer import FileUploadSerializer

class FileUploadView (APIView):

    def post(self, request, format:None):
        serializer = FileUploadSerializer(data = request.data)
        process_file.delay(serializer.data['file'].id, serializer.data['table_name'])
        if serializer.is_valid():
            #Store file, send message to data processing service
            return Response({'message':'File uploaded successfully'}, status=status.HTTP_201_CREATED, status_code=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)