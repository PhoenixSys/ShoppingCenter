from django.contrib import admin

# Register your models here.
from orders.models import OrderItem, Order


class CustomAdmin(admin.ModelAdmin):
    search_fields = ["id"]


admin.site.register(Order, CustomAdmin)
admin.site.register(OrderItem, CustomAdmin)
