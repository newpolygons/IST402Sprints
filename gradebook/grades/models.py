from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length = 100)
    grade = models.CharField(max_length= 10)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
