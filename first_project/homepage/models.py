from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length = 130)
    last_name = models.CharField(max_length = 130)
    