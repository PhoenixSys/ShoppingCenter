from django.urls import path

from customers.views import CostumerManagerApi

urlpatterns = [
    path('', CostumerManagerApi.as_view(), name="api_costumers"),
]