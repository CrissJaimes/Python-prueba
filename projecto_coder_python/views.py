from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from Desafio import *

def saludo(request):
    return HttpResponse("Hola Coder uwu")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)


def calcular_año_de_nacimiento(request, edad):
    cuenta = datetime.now().year - int(edad)
    respuesta = f"Tu año de nacimiento es {cuenta}"
    return HttpResponse(respuesta)

def vista_plantilla(request):
    archivo = open(r"C:\Users\JoseJ\OneDrive\Escritorio\CoderHouse\Python\python\projecto_coder_python\projecto_coder_python\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
