from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('<int:pk>/toggle/', views.toggle_task_completion, name='task_toggle'),
    path('tasks/<int:task_id>/toggle/', views.toggle_task_completion, name='toggle_task_completion'),
]

