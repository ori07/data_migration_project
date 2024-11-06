from rest_framework import serializers

# Class to process the parameter for upload file service
class FileUploadSerializer(serializers.Serializer):
        file = serializers.FileField()
        table_name = serializers.CharField(max_length=100)