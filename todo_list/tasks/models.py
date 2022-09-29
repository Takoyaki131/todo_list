from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length = 25)
    task_description = models.CharField(max_length = 50)