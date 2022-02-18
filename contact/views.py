from django.contrib import messages
from django.contrib.messages import get_messages
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
            messages.add_message(request, messages.SUCCESS, "SUCCESS")
        except:
            messages.add_message(request, messages.ERROR, "ERROR")
        return redirect("contact")