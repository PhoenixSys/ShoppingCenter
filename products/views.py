from django.shortcuts import render

# Create your views here.
from django.views import View


class ProductsView(View):
    def get(self, request):
        return render(request, "_layout/cards.html")
