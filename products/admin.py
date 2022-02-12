from django.contrib import admin

# Register your models here.
from products.models import Products, Categories, Discount

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Discount)