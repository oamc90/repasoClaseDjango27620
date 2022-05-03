import http
from statistics import median
from django.http import HttpResponse
import datetime

from django.template import Context , Template , loader

def saludo(request):
    return HttpResponse("Hola mundo")

def segundavista(request):
    return HttpResponse("<br><h2>vamos avanzando")

def diadehoy(request):
    dia=datetime.datetime.now()
    cadena="<h1> Hoy es : "+str(dia)+"</h1>"
    return HttpResponse(cadena)

def saludoconnombre(self,nombre):
    return HttpResponse( "<h1> Hola mi nombre es : "+nombre+"<h1/>")

def nacimiento(self,edad):
    return HttpResponse("<h1> Tu año de nacimiento es: " +str(datetime.datetime.now().year-int(edad))+"</h1>")


def probandohtml(self):
    nom="oscar"
    ape="medina"
    lista_notas=[10,15,18,20]

    diccionario={"nombre" : nom , "apellido" : ape, "lista": lista_notas}

    plantilla=loader.get_template("template1.html")

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


