from django.urls import path
from customers.views import TestTemplates, TestTemplates1

urlpatterns = [
    path('test/', TestTemplates.as_view() , name="test1"),
    path('test1/', TestTemplates1.as_view()),
]
