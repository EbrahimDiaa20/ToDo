from django.urls import path
from .views import to_do,Home

urlpatterns = [
    path('', Home, name='home'),
    path('todo/', to_do, name='todo'),


]
