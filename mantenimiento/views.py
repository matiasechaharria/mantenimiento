from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Instituto,Departamento,Servicio,Sector, Contacto
from .forms import ContactoForm
# Create your views here.

from django.http import HttpResponse




def home(request):
    return render(request, "home.html")

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

def Contactof(request):
    form=ContactoForm()
    if request.method=='POST':
        form=ContactoForm(request.POST)
        if form.is_valid():
            Contacto.objects.create(**form.cleaned_data)

    context ={'form':form}
    return render(request, 'form_generica.html',context)

#django rest framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
