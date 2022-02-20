from django.urls import path

from customers.views import RegisterLoginView

urlpatterns = [
    path('login/', RegisterLoginView.as_view(), name="RegisterLoginView"),
]
