from django.db import models

# Create your models here.
class PostModel(models.Model):
    userid=models.CharField(max_length=100,default="")
    title=models.CharField(max_length=100,default="")
    message=models.TextField()