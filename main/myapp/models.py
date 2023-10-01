from django.db import models

# Create your models here.
class Service(models.Model):
    iocn = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    des = models.TextField()