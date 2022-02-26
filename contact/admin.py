from django.contrib import admin

# Register your models here.
from contact.models import ContactUs


class CustomAdminContactUs(admin.ModelAdmin):
    search_fields = ["id", "name", "email", "text"]
    list_display = ["id", "name", "email", "text"]


admin.site.register(ContactUs, CustomAdminContactUs)
