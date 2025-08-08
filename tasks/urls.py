from django.urls import path

from .views import (
    TaskListView, 
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete')
]