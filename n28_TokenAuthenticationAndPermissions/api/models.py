from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)

from django.conf import settings
from  django.db.models.signals import  post_save
from django.dispatch import receiver
from  rest_framework.authtoken.models import Token

#this Signal created auth token for users 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)