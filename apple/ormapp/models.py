
from django.db import models
from django.contrib import admin

class FoodApp(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Date = models.DateField()
    ItemName = models.CharField(max_length=100)
    Amount = models.FloatField()
    

class FoodAppAdmin(admin.ModelAdmin):
    list_display = (
        'OrderID',
        'Name',
        'Date',
        'ItemName',
        'Amount',
    )


# Create your models here.
