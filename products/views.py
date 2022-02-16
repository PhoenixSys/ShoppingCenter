from django.shortcuts import render

# Create your views here.
from django.views import View

from products.models import Products


class ProductsView(View):
    def get(self, request):
        datas = Products.objects.all()
        context = {
            "datas": datas
        }
        return render(request, "_layout/cards.html", context=context)

    def post(self, request):
        print(request.POST)
        return request.POST[0]["name"]
