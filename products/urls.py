from django.urls import path

from products.views import ProductsView, ProductApi

urlpatterns = [
    path('', ProductsView.as_view(), name="home"),
    path('api/', ProductApi.as_view(), name="ProductApi"),

]
