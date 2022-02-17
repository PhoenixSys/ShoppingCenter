from django.urls import path

from products.views import ProductsView, ProductApi, ProductApiSammi

urlpatterns = [
    path('', ProductsView.as_view(), name="home"),
    path('api/', ProductApi.as_view(), name="ProductApi"),
    path('apisammi/<int:pk>', ProductApiSammi.as_view(), name="ProductApiSammi"),

]
