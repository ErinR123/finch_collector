from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
   
    