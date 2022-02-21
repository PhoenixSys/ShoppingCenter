from django.urls import path

from orders.views import OrderApiView

urlpatterns = [
    path('order_api/', OrderApiView.as_view(), name="order_api"),
]
