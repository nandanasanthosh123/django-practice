from django.db import models

# Create your models here.

class filedetails(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField