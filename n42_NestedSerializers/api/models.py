from django.db import models

# Create your models here.

class Singer(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'FeMale'),
    )
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=30)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='sungby')
    duration = models.IntegerField()        

    def __str__(self):
        return self.title