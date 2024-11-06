from django.db import models

class Job(models.Model):
    # The primary key will auto-increment by default
    #id = models.IntegerField(primary_key=True)
    job = models.CharField(max_length=100)

class Department(models.Model):
    # The primary key will auto-increment by default
    #id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=100)

class Hired_Employee(models.Model):
    # The primary key will auto-increment by default
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    datetime = models.CharField(max_length=30)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)