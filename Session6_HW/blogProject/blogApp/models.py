from django.db import models

# Create your models here.

class Article (models.Model):
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=40, null=True)
    content = models.TextField(null=True)
    create_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
