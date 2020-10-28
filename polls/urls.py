from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mensaje', views.mensaje, ),
    path('prueba', views.prueba, ),
    path('prueba2', views.prueba2, ),
]
