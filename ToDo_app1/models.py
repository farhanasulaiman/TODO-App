from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    date = models.DateField()
