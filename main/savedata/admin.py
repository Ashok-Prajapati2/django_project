from django.contrib import admin
from .models import Savedata  # Import your model

class savedataAdmin(admin.ModelAdmin):
    list_display = ('usertitle','userdest')  # Define the fields to display in the admin list view

# Register the model with the admin class
admin.site.register(Savedata, savedataAdmin)
