from django.urls import path, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('subirnota',views.SubirNota,name='subirnota'),
    path('listNotas',views.MostrarNotas, name='MostrarNotas'),
]
