from django.urls import path
from customers.views import TestTemplates

urlpatterns = [
    path('test/', TestTemplates.as_view()),
]
