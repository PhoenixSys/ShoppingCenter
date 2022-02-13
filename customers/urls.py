from django.urls import path, include

from customers.views import TestTemplates

urlpatterns = [
    path('test/', TestTemplates.as_view()),
]
