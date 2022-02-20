from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages import get_messages, add_message
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from customers.models import Costumers


class RegisterLoginView(View):
    def get(self, request):
        return render(request, "customers/register_login_page.html")

    def post(self, request):
        data = request.POST
        user = User.objects.create_user(username=data["phone"], email=data["email"], password=data["password"],
                                        phone=data["phone"])
        costumer = Costumers.objects.create(user=user)
        print(costumer.id)
        return redirect("register")
