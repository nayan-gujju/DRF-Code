from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=30)