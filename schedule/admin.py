from django.contrib import admin

# Register your models here.

from .models import event, presence

admin.site.register(event)
admin.site.register(presence)