from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import UserManager
from django.forms import ModelForm
from django.forms.models import modelform_defines_fields

from core.models import User

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
admin.site.register(User, UserAdmin)
