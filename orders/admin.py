from django.contrib import admin

# Register your models here.
from orders.models import OrderItem, Order, Transactions


class CustomAdminOrder(admin.ModelAdmin):
    search_fields = ["id", "costumer", "status"]
    list_display = ["id", "costumer", "status", "is_paid"]


class CustomAdminOrderItem(admin.ModelAdmin):
    search_fields = ["id", "order", "item", "quantity"]
    list_display = ["id", "order", "item", "quantity"]


class CustomAdminTransactions(admin.ModelAdmin):
    search_fields = ["id", "order", "transactionId", "transactionLink"]
    list_display = ["id", "order", "transactionId", "transactionLink"]


admin.site.register(Order, CustomAdminOrder)
admin.site.register(OrderItem, CustomAdminOrderItem)
admin.site.register(Transactions, CustomAdminTransactions)
