from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Savedata(models.Model):
   
    usertitle = models.CharField(max_length=20)
    userdest = HTMLField()
    