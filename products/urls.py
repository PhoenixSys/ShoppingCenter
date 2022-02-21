from django.urls import path

from products.views import ProductsView, ProductApiDestroy, ProductApiList, ProductApiCreate, ProductsCategoryView

urlpatterns = [
    path('', ProductsView.as_view(), name="home"),
    path('cateyory/<int:id>', ProductsCategoryView.as_view(), name="category_view"),
    path('product_create/', ProductApiCreate.as_view(), name="ProductApiCreate"),
    path('product_list/<int:pk>', ProductApiList.as_view(), name="ProductApiList"),
    path('product_delete/<int:pk>', ProductApiDestroy.as_view(), name="ProductApiDestroy"),

]
