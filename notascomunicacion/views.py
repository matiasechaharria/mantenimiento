from django.shortcuts import render
from .forms import NotaComunicacionForm
from .models import NotaComunicacion
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
# Create your views here.

def SubirNota(request):
    form=NotaComunicacionForm()

    if request.method=='POST':
        form=NotaComunicacionForm(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            print(form.cleaned_data)
            NotaComunicacion.objects.create(**form.cleaned_data)

        else:
            print("no es valid")
            print(form.errors)

    context={'form':form}
    return render(request, 'form_generica.html',context)

def MostrarNotas(request):
    notas= NotaComunicacion.objects.all()
    context={"notas":notas}
    return render(request,'listNotasComunicacion.html',context)
