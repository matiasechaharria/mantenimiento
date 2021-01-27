from django.urls import path, path
from rest_framework import routers
from . import views

urlpatterns = [

    path('listaProveedor',views.MostrarProveedor, name='listaProveedor'),
]
