from django.contrib import admin
from .models import Products, Order

# Register models in admin
admin.site.register(Products)
admin.site.register(Order)