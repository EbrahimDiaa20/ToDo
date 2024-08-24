from django.urls import path
from .views import to_do

urlpatterns = [
    path('', to_do, name='submit'),
]
