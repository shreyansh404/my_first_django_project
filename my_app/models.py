from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField(max_length=200,default='')