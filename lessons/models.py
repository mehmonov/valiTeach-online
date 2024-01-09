from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 200,unique = True) 
    description = models.TextField()
    price = models.FloatField()
    teacher = models.CharField(max_length = 200)
    coupon = models.CharField(max_length= 100, null=True, blank=True)
    def __str__(self):
      return "{}".format(self.name)
  
class Lesson(models.Model):
    name = models.CharField(max_length = 200) 
    course = models.ForeignKey(Course,  on_delete=models.CASCADE,
        related_name="lessons",)
    link = models.CharField(max_length=250)
    def __str__(self):
      return f"{self.course.name} --- {self.name}"
  