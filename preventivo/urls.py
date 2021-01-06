from django.urls import path

from . import views

urlpatterns = [

    path('home', views.Home, name='home'),
    path('carga', views.Carga, name='carga'),
    path('consulta', views.Consulta, name='consulta'),
    path('todos', views.TodosPreventivos.as_view(), name='TodosPreventivos'),

]
