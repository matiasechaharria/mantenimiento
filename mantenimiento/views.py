from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Instituto,Departamento,Servicio,Sector, Contacto
# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def Clientes(request):
    """
    muestra la tabla de instituto,departamento,servicio,sector
    """
   # renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clientes.html'
    cliente = Servicio.objects.all()
    return render(request, 'clientes.html', {'cliente':cliente})

def Contactos(request):
    """
    muestra los contactos de cadad sector
    """

    Contactos = Contacto.objects.all()
    return render(request, 'contactos.html', {'Contactos':Contactos})