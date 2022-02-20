from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages import get_messages, add_message
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from customers.models import Costumers
from products.models import Categories


class RegisterLoginView(View):
    def get(self, request):
        categories = Categories.objects.all()
        context = {
            "categories": categories
        }
        return render(request, "customers/register_login_page.html", context=context)

    def post(self, request):
        data = request.POST
        user = User.objects.create_user(username=data["phone"], email=data["email"], password=data["password"],
                                        phone=data["phone"])
        costumer = Costumers.objects.create(user=user)
        print(costumer.id)
        return redirect("register")


class Profile(PermissionRequiredMixin, View):
    permission_required = ["authenticated"]

    def get(self, request):
        categories = Categories.objects.all()

        user = request.user
        context = {
            "userInfo": user,
            "categories": categories
        }
        return render(request, "customers/profile.html", context=context)
