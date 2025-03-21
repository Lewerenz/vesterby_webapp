from django.contrib import admin

# Register your models here.

from .models import Event, Visit

admin.site.register(Event)
admin.site.register(Visit)