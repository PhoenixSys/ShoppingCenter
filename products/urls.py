from django.urls import path

from products.views import *

urlpatterns = [
    path('', ProductsView.as_view(), name="home"),
    path('cateyory/<int:id>', ProductsCategoryView.as_view(), name="category_view"),
    path('search/<str:query>', SearchProducts.as_view(), name="search_query"),
    path('have_discount/', HaveDiscount.as_view(), name="have_discount"),
    path('product/id/<int:id>', ProductDetailView.as_view(), name="product_detail"),
    path('product_create/', ProductApiCreate.as_view(), name="ProductApiCreate"),
    path('product_list/<int:pk>', ProductApiList.as_view(), name="ProductApiList"),
    path('product_delete/<int:pk>', ProductApiDestroy.as_view(), name="ProductApiDestroy"),

]
