from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    image = models.ImageField(upload_to='users')
    city = models.CharField(max_length=30)