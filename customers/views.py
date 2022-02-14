from django.shortcuts import render

# Create your views here.
from django.views import View


class TestTemplates(View):
    def get(self, request):
        return render(request, "_layout/cards.html")

class TestTemplates1(View):
    def get(self, request):
        return render(request, "_layout/_base.html")
