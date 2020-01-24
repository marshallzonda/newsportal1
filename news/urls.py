from django.urls import path
from .views import create, delete, index, edit, details


urlpatterns = [
    path('', index),
    path('create', create),
    path('edit', edit),
    path('index', index),
    path('details',details),
    path('delete',delete),
]