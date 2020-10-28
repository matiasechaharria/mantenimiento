from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def mensaje(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def prueba(request):
    template = loader.get_template('polls/prueba.html')
    return HttpResponse(template.render())

def prueba2(request):

    return render(request,'polls/prueba.html')
