from django.shortcuts import render
from django.http import HttpResponse
from Desafio.models import Familiares
from django.template import loader, Template, Context

# Create your views here.



def listadoFamiliares(request):

    listaFamiliares = Familiares.objects.all()

    datos = {
        "listaFamiliares": listaFamiliares,

    }

    archivo = open(r"C:\Users\JoseJ\OneDrive\Escritorio\CoderHouse\Python\python\projecto_coder_python\Desafio\Template.html")
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context(datos)
    doc = plantilla.render(contexto)
    
    return HttpResponse(doc)