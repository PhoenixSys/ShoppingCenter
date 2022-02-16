from django.http import HttpResponse
from django.shortcuts import render
import json
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
        data = json.loads(request.body)
        product_name = data[0]["name"]
        product_price = data[0]["price"]
        product_count = data[0]["count"]
        print(product_name, product_price, product_count)
        return HttpResponse("ok", 200)
