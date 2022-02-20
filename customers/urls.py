from django.urls import path

from customers.views import RegisterLoginView

urlpatterns = [
    path('register/', RegisterLoginView.as_view(), name="register"),
]
