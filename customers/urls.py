from django.urls import path

from customers.views import RegisterLoginView, Profile, LogOutCostumer

urlpatterns = [
    path('register/', RegisterLoginView.as_view(), name="register"),
    path('profile/', Profile.as_view(), name="profile"),
    path('logout/', LogOutCostumer.as_view(), name="logout"),
]
