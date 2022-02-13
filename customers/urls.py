from django.urls import path
from customers.views import TestTemplates, TestTemplates1

urlpatterns = [
    path('test/', TestTemplates.as_view()),
    path('test1/', TestTemplates1.as_view()),
]
