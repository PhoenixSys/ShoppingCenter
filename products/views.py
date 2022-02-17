from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
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


class ProductApi(APIView):
    def get(self, request):
        product_ser = ProductSerializer(instance=Products.objects.all(), many=True)
        return Response(product_ser.data, status=200)

    def post(self, request):
        data = request.POST
        product_ser = ProductSerializer(data=data)
        if product_ser.is_valid():
            new_product = product_ser.save()
            return Response(new_product.id, status=201)
        else:
            return JsonResponse(product_ser.errors, status=400)


class ProductApiSammi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
