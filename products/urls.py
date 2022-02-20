from django.urls import path

from products.views import ProductsView, ProductApiDestroy, ProductApiList, ProductApiCreate

urlpatterns = [
    path('', ProductsView.as_view(), name="home"),
    path('product_create/', ProductApiCreate.as_view(), name="ProductApiCreate"),
    path('product_list/<int:pk>', ProductApiList.as_view(), name="ProductApiList"),
    path('product_delete/<int:pk>', ProductApiDestroy.as_view(), name="ProductApiDestroy"),

]
