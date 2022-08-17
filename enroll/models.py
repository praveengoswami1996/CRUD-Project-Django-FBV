from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length=50)
    studentEmail = models.EmailField(max_length=100)
    studentPassword = models.CharField(max_length=50)
