from django.contrib import admin

# Register your models here.
from orders.models import OrderItem, Order


class CustomAdminOrder(admin.ModelAdmin):
    search_fields = ["id", "costumer", "status"]
    list_display = ["id", "costumer", "status", "is_paid"]


class CustomAdminOrderItem(admin.ModelAdmin):
    search_fields = ["id", "order", "item", "quantity"]
    list_display = ["id", "order", "item", "quantity"]


admin.site.register(Order, CustomAdminOrder)
admin.site.register(OrderItem, CustomAdminOrderItem)
