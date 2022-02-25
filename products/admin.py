from django.contrib import admin

# Register your models here.
from products.models import Products, Categories, Discount


class CustomAdminProducts(admin.ModelAdmin):
    search_fields = ["id", "name", "price", "discount"]
    list_display = ["id", "name", "price", "discount"]


class CustomAdminCategories(admin.ModelAdmin):
    search_fields = ["id", "type", "parent"]
    list_display = ["id", "type", "parent"]


class CustomAdminDiscount(admin.ModelAdmin):
    search_fields = ["id", "type", "value", "max_price"]
    list_display = ["id", "type", "value", "max_price"]


admin.site.register(Products, CustomAdminProducts)
admin.site.register(Categories, CustomAdminCategories)
admin.site.register(Discount, CustomAdminDiscount)
