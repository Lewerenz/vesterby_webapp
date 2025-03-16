from django.contrib import admin
from .models import Expense, CostCenter, Sharing

# Register your models here.

admin.site.register(Expense)
admin.site.register(CostCenter)
admin.site.register(Sharing)