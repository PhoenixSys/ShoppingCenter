from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View


class RegisterLoginView(View):
    def get(self, request):
        return render(request, "customers/register_login_page.html")
