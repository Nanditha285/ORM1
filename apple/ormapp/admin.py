from django.contrib import admin
from .models import FoodApp, FoodAppAdmin

admin.site.register(FoodApp, FoodAppAdmin)

# Register your models here.
