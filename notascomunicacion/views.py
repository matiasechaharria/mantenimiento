from django.shortcuts import render
from .forms import NotaComunicacionForm
# Create your views here.

def SubirNota(request):
   form=NotaComunicacionForm()
   context={'form':form}
   return render(request, 'form_generica.html',context)

