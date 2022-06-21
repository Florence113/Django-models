from datetime import datetime
from distutils.text_file import TextFile
from enum import auto
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(datetime.now())
    Published_date = models.DateTimeField(auto)
    
    def __str__(self) -> str:
        return self.Title