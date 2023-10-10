from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.
class news(models.Model):
   
    title = models.CharField(max_length=20)
    des = models.TextField(max_length=1000)
    dest = HTMLField()
    
    
    news_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
