from django.shortcuts import render
from .forms import NotaComunicacionForm
from .models import NotaComunicacion
# Create your views here.

def SubirNota(request):
    form=NotaComunicacionForm()

    if request.method=='POST':
        form=NotaComunicacionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            NotaComunicacion.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context={'form':form}
    return render(request, 'form_generica.html',context)
