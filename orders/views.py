from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Costumers
from orders.models import Order, OrderItem
from orders.serializer import OrderSerializer, OrderItemsSerializer, ItemSerializer
from products.models import Products, Categories


class OrderApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_ser = OrderSerializer(instance=Order.objects.all(), many=True)
        order_items_ser = OrderItemsSerializer(instance=OrderItem.objects.all(), many=True)
        content = {
            "orders": order_ser.data,
            "order_item": order_items_ser.data,
            "user": request.user.id
        }
        return Response(content)

    def post(self, request):
        user = request.user
        costumer = Costumers.objects.get(user=user)
        if costumer.default_address is not None:
            order = Order.objects.create(costumer=costumer, address_id=costumer.default_address.id)
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
                    else:
                        print(order_f.errors)
            return Response({"result": "SUCCESS"})
        else:
            return Response({"error": "Please Select A valid Default Address !"}, status=401)


class OrderHistory(PermissionRequiredMixin, View):
    permission_required = ["core.authenticated"]

    def get(self, request):
        user = request.user
        costumer = Costumers.objects.get(user=user)
        orders = Order.objects.filter(costumer=costumer)
        context = {
            "orders": orders,
        }
        return render(request, "orders/full_history.html", context)
