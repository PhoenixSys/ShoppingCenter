from django.contrib import admin

# Register your models here.

from customers.models import Costumers, Addresses


class CustomAdminCustomer(admin.ModelAdmin):
    search_fields = ["id", "user", "default_address"]
    list_display = ["id", "user", "default_address"]


class CustomAdminAddress(admin.ModelAdmin):
    search_fields = ["id", "state", "city", "postal_code"]
    list_display = ["id", "state", "city", "postal_code"]


admin.site.register(Costumers, CustomAdminCustomer)
admin.site.register(Addresses, CustomAdminAddress)
