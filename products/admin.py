from django.contrib import admin

# Register your models here.
from products.models import Products, Categories, Discount


class CustomAdmin(admin.ModelAdmin):
    search_fields = ["id"]


admin.site.register(Products, CustomAdmin)
admin.site.register(Categories, CustomAdmin)
admin.site.register(Discount, CustomAdmin)
