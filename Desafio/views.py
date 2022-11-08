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

    plantilla = loader.get_template("Template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)