from django.contrib import admin

# Register your models here.
from customers.models import Costumers, Addresses

admin.site.register(Costumers)
admin.site.register(Addresses)
