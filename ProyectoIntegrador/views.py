from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ProyectoIntegrador.models import *
from ProyectoIntegrador.forms import *

# Create your views here.

from django.http import JsonResponse

from .importService import importService


def importWorldPopulationData(request):
    formPoblacion = FormPoblacion()
    if request.method == 'POST':
        formPoblacion = FormPoblacion(request.POST)
        if formPoblacion.is_valid():
            formPoblacion.search()
            return redirect('blog_buscar_pais')
    return render(request, 'blog/buscar.html', {'formPoblacion': formPoblacion})
    
def blog_inicio(request):
    return render(request, 'blog/index.html')


def blog_about(request):
    return render(request, 'blog/about.html')

def blog_buscar_pais(request):
    return render(request, 'blog/buscar.html')

def scrapping(request):
    return render(request= request, template_name= 'blog/scrapping.html')


