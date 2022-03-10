from django.urls import path

from orders.views import OrderApiView, OrderApiTest

urlpatterns = [
    path('order_api/', OrderApiView.as_view(), name="order_api"),
    path('orderitem_list/<int:id>', OrderApiTest.as_view(), name="orderitem_list"),
]
