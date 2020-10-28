from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cliente', views.Clientes, name='cliente'),
    path('contactos', views.Contactos, name='contactos'),

]
