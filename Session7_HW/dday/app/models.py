from pickle import TRUE
from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
