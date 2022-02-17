from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.views import APIView

from products.models import Products
from products.serializer import ProductSerializer


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
        response = JsonResponse({"status_code": 200})
        response.status_code = 200
        return response


# @csrf_exempt
# def ProductApi(request):
#     if request.method == "GET":
#         product_ser = ProductSerializer(instance=Products.objects.all(), many=True)
#         print(product_ser)
#         print(product_ser.data)
#         return JsonResponse({'data': product_ser.data}, status=200)
#
#     if request.method == "POST":
#         data = request.POST
#         product_ser = ProductSerializer(data=data)
#         if product_ser.is_valid():
#             new_product = product_ser.save()
#             return JsonResponse({'obj': new_product.id}, status=201)
#         else:
#             return JsonResponse({"error : ": product_ser.errors}, status=400)
#     else:
#         return JsonResponse({}, status=400)
