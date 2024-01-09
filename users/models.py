from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    status = (
      ('User', 'User'),
      ('Admin', 'Admin')
    )
    phone = models.CharField(max_length = 50,unique = True, null=True, blank=True)
    location = models.CharField(max_length = 100, null=True, blank=True )
    start_course = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(choices=status, default='User')
    
    def __str__(self):
      return "{}".format(self.username)