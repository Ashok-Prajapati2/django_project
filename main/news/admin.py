from django.contrib import admin
from news.models import news
class sadmin(admin.ModelAdmin):
    list_display=('title','des')
admin.site.register(news,sadmin)