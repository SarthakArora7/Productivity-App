from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddTask.as_view(), name="add_task"),
    path("view/", views.ViewTask.as_view(), name="view_tasks")
]
