from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Preventivo
from datetime import datetime

# Create your views here.

from django.http import HttpResponse
from .forms import PreventivoForm

def Home(request):
    return render(request, 'todos_preventivo.html')

def Carga(request):
    if request.method == "POST":
        form = PreventivoForm(request.POST)
        if form.is_valid():
           # form.dateTime = datetime.now()
            form.save()
            return redirect('consulta')

    else:

         form = PreventivoForm()
    return render(request, 'Carga_preventivo.html', {'form': form})






def Consulta(request):


    todo = Preventivo.objects.all()
    return render(request, 'todos_preventivo.html', {'preventivos': todo})

