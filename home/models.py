
from django.db import models

from lessons.models import Course
from users.models import User
import secrets
def token_generator():
    """
        15 belgi uzunligida token qaytaradi
    """
    token = secrets.token_hex(15)
    
    return token
    

class Tokens(models.Model):
    token = models.CharField(max_length= 200)
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users",
    )
    start_date  = models.DateField(auto_now_add=True)

    expiration_time = models.DateField() 
    
    def __str__(self):
      return f"{self.course} -- {self.user}"
  
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_generator()  
        super().save(*args, **kwargs)