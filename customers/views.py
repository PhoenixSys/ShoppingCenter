from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.messages import get_messages, add_message
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from customers.models import Costumers, Addresses
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
        try:
            user = User.objects.create_user(username=data["phone"], email=data["email"], password=data["password"],
                                            phone=data["phone"])
            perm = Permission.objects.get(codename="authenticated")
            user.user_permissions.add(perm)
            Costumers.objects.create(user=user)
            send_mail(
                'Congratulations !',
                f'Dear Friend , Thanks For Join Us !\nBest Regards',
                from_email=None,
                recipient_list=[f"{user.email}"],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, "SUCCESS")
        except Exception as e:
            messages.add_message(request, messages.ERROR, "ERROR")
        return redirect("home")


class Profile(PermissionRequiredMixin, View):
    permission_required = ["core.authenticated"]

    def get(self, request):
        user = request.user
        categories = Categories.objects.all()
        costumers = Costumers.objects.get(user_id=user.id)
        addresses = Addresses.objects.filter(costumer_id=costumers.id).all()
        context = {
            "userInfo": user,
            "categories": categories,
            "addresses": addresses
        }
        return render(request, "customers/profile.html", context=context)

    def post(self, request):
        data = request.POST
        print(data)
        print(data["first_name"])
        print(data["default_address"])
        return redirect("home")
