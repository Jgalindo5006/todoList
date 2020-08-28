from django.db import models


# Create your models here.
class Todo(models.Model):
    current_date = models.DateTimeField()
    text_list = models.CharField(max_length=200)
