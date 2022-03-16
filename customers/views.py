from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages import get_messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from customers.models import Costumers, Addresses
from orders.models import Order
import re


class RegisterLoginView(View):
    def get(self, request):
        return render(request, "customers/register_login_page.html")

    def post(self, request):
        data = request.POST
        try:
            pattern_email = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
            email_validator = re.fullmatch(pattern_email, data["email"])
            pattern_phone = "^(9|(09))(((1)|(3))([0-9])|(20)|(21))(\d{7})"
            phone_validator = re.fullmatch(pattern_phone, data["phone"])
            if email_validator and phone_validator:
                user = User.objects.create_user(username=data["phone"], email=data["email"], password=data["password"],
                                                phone=data["phone"])
                content = ContentType.objects.get_for_model(User)
                Permission.objects.get_or_create(codename="authenticated", name="Can See Profile",
                                                 content_type=content)
                perm = Permission.objects.get(codename="authenticated")
                user.user_permissions.add(perm)
                user.save()
                Costumers.objects.create(user=user)
                send_mail(
                    'Congratulations !',
                    f'Dear Friend , Thanks For Join Us !\nBest Regards',
                    from_email=None,
                    recipient_list=[f"{user.email}"],
                    fail_silently=False,
                )
                user_logged = authenticate(username=user.username, password=data["password"])
                login(request, user_logged)
                messages.add_message(request, messages.SUCCESS, "You Are Successfully Registered !")
            else:
                messages.add_message(request, messages.ERROR, "Register Failed ! Please Check Email/Phone Values")
        except Exception as e:
            messages.add_message(request, messages.ERROR, f"Register Failed ! Please Check Input's Data")
        message = get_messages(request)
        return render(request, "customers/register_login_page.html", context={"messages": message})


class Profile(PermissionRequiredMixin, View):
    permission_required = ["core.authenticated"]

    def get(self, request):
        user = request.user
        costumer = Costumers.objects.get(user_id=user.id)
        orders = Order.objects.filter(costumer=costumer)[:3]
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
            if costumers.default_address_id is None:
                costumers.default_address_id = Addresses.objects.get(postal_code=data["postal_code"])
                costumers.save()
        return redirect("home")
