from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages import get_messages, add_message
from django.core.mail import send_mail
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
        try:
            user = User.objects.create_user(username=data["phone"], email=data["email"], password=data["password"],
                                            phone=data["phone"])
            costumer = Costumers.objects.create(user=user)
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
    permission_required = ["authenticated"]

    def get(self, request):
        categories = Categories.objects.all()

        user = request.user
        context = {
            "userInfo": user,
            "categories": categories
        }
        return render(request, "customers/profile.html", context=context)
