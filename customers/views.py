from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.messages import get_messages, add_message
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from customers.models import Costumers, Addresses
from orders.models import Order
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
        costumer = Costumers.objects.get(user_id=user.id)
        orders = Order.objects.filter(costumer=costumer)[:3]
        print(orders)
        addresses = Addresses.objects.filter(costumer=costumer).all()
        context = {
            "userInfo": costumer,
            "addresses": addresses,
            "orders": orders
        }
        return render(request, "customers/profile.html", context=context)

    def post(self, request):
        data = request.POST
        user = request.user
        costumers = Costumers.objects.get(user=user)
        if "first_name" in data.keys():
            user.first_name = data["first_name"]
            user.save()
        if "last_name" in data.keys():
            user.last_name = data["last_name"]
            user.save()
        if "default_address" in data.keys():
            costumers.default_address_id = data["default_address"]
            costumers.save()
        if len(data["state"]) >= 3 and len(data["city"]) >= 3 and len(data["postal_code"]) >= 3:
            Addresses.objects.get_or_create(costumer=costumers, state=data["state"], city=data["city"],
                                            postal_code=data["postal_code"])
        return redirect("home")
