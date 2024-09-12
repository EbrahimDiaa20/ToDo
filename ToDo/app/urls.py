from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_todo, name='add_todo'),
    path('', views.view_todos, name='view_todos'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
