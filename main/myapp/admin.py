from django.contrib import admin
from myapp.models import Service
class sadmin(admin.ModelAdmin):
    list_display=('iocn','title','des')
admin.site.register(Service,sadmin)