from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from core.models import User, IpManagerDb

UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name', 'email')
UserAdmin.ordering = ('phone',)
UserAdmin.fieldsets[0][1]['fields'] = ('phone', 'password')
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('phone', "username", "email", 'password1', 'password2'),
    }),
)


class CustomAdminIpManager(admin.ModelAdmin):
    search_fields = ["id", "ip", "views", "access"]
    list_display = ["id", "ip", "views", "access"]


admin.site.register(User, UserAdmin)
admin.site.register(IpManagerDb, CustomAdminIpManager)
