from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    
    STATUS = {
        ('regular', 'regular'),
        ('admin', 'admin'),
    }

    email = models.EmailField(unique = True)
    status = models.CharField(max_length=255, choices = STATUS, default = 'regular')
    description = models.TextField('Description', max_length=255, default = '', blank = True)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.username
    