from django.db import models


# Create your models here.
class Todo(models.Model):
    added_date = models.DateTimeField()
    text_list = models.ChardField(max_lenght=200)
