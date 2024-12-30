from django.urls import path
from .views import ListTodoAPI, TodoAPI

urlpatterns = [
    path('todo/', ListTodoAPI.as_view(), name="fetch_all_todos"),
    path('todo/<int:pk>/', TodoAPI.as_view(), name='todo')
]