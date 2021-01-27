from django.urls import path

from . import views

from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #path('', include(router.urls)),
#    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    #path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('cliente', views.Clientes, name='cliente'),
    path('AContacto',views.Contactof,name='AltaContacto'),
    path('LContacto', views.Contactos, name='ListarContacto'),

]
