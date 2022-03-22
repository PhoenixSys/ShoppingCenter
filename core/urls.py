from django.urls import path

from core.views import BackGroundTasks

urlpatterns = [
    path('start/', BackGroundTasks.as_view(), name="start_tasks"),
    path('end/', BackGroundTasks.as_view(), name="end_tasks"),
]
