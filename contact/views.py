from django.contrib import messages
from django.contrib.messages import get_messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from contact.models import ContactUs


class ContactView(View):
    def get(self, request):
        message = get_messages(request)
        context = {
            "messages": message
        }
        return render(request, "contact/ContactUs.html", context=context)

    def post(self, request):
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        text = data.get("text")
        try:
            ContactUs.objects.create(name=name, email=email, text=text)
            send_mail(
                'Configuration !',
                'Your Message Received !',
                from_email=None,
                recipient_list=[f"{email}"],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, "SUCCESS")
        except Exception as e:
            messages.add_message(request, messages.ERROR, f"ERROR | {e}")
        return redirect("contact")


class AboutUs(View):
    def get(self, request):
        return render(request, "contact/AboutUs.html")
