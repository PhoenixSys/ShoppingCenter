from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Costumers
from orders.models import Order, OrderItem
from orders.serializer import OrderSerializer, OrderItemsSerializer, ItemSerializer
from products.models import Products


class OrderApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        order_ser = OrderSerializer(instance=Order.objects.all(), many=True)
        order_items_ser = OrderItemsSerializer(instance=OrderItem.objects.all(), many=True)
        content = {
            "orders": order_ser.data,
            "order_item": order_items_ser.data,
            "user": request.user.id
        }
        return Response(content)

    def post(self, request, format=None):
        costumer = Costumers.objects.get(id=10)
        order = Order.objects.create(costumer=costumer)
        check = ItemSerializer(data=request.data, many=True)
        if check.is_valid():
            for i in request.data:
                i["order"] = order.id
                item = Products.objects.get(name=i["name"].replace("_", " "))
                i["item"] = item.id
                i["quantity"] = i["count"]
                del i["name"]
                del i["price"]
                del i["count"]
                order_f = OrderItemsSerializer(data=i)
                if order_f.is_valid():
                    order_f.save()
                    return Response({"order": order_f.data})
                else:
                    print(order_f.errors)
        return Response({})
