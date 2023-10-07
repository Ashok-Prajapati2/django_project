from django.db import models
# Create your models here.
class news(models.Model):
   
    title = models.CharField(max_length=20)
    des = models.TextField()