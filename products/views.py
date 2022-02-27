from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Products, Categories
from products.serializer import ProductSerializer


class ProductsView(View):
    def get(self, request):
        datas = Products.objects.all()
        context = {
            "datas": datas,
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


class ProductApiCreate(APIView):
    def post(self, request):
        data = request.POST
        product_ser = ProductSerializer(data=data)
        if product_ser.is_valid():
            new_product = product_ser.save()
            return Response(new_product.id, status=201)
        else:
            return JsonResponse(product_ser.errors, status=400)


class ProductApiList(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ProductApiDestroy(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


class ProductsCategoryView(View):
    def get(self, request, id):
        datas = Products.objects.filter(category__products=1)
        context = {
            "datas": datas,
        }
        return render(request, "_layout/cards.html", context=context)


class ProductDetailView(View):
    def get(self, request, id):
        product = Products.objects.get(id=id)
        context = {
            "product": product,
        }
        return render(request, "_layout/details.html", context=context)
