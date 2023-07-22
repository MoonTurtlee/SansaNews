from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import API
from .iniciativas import INICIATIVAS
from . import forms
from . import models
import os
import json
import datetime


def home(request):
    recientes = API.recientes(4)
    return render(request,"Home.html",{"primera": [recientes[0]],"publicaciones": recientes[1:], "iniciativas": INICIATIVAS})

def iniciativa(request, usuario):
    with open(os.path.dirname(os.path.dirname(__file__)) + f"/static/iniciativas/biografias.json", "r", encoding='utf-8') as archivo:
        biografias = json.load(archivo)
        biografia = biografias[usuario]

    publicaciones= API.contenido(usuario)

    return render(request, "Molde.html", {
        "usuario": usuario,
        "nombre": INICIATIVAS[usuario],
        "biografia": biografia,
        "key": publicaciones,
        "iniciativas": INICIATIVAS
    })

def about(request):
    return render(request,"about.html")

def avisos(request):
    lista = models.imagenes_avisos.objects.all().order_by("id").reverse()
    lista.reverse()
    return render(request,"Avisos.html",{"key": lista, "iniciativas": INICIATIVAS})

def subir_avisos(request, id=None):
    imagen = forms.avisos_forms(request.POST, request.FILES)

    if request.method == "POST":
        if imagen.is_valid():
            imagen.save()
            return redirect(avisos)
    context = {"imagen": imagen, "iniciativas": INICIATIVAS}
    return render(request, 'Subir_Avisos.html', context)

def test(request):
    biografias = {}

    for iniciativa in INICIATIVAS:
        biografias[iniciativa] = API.actualizar_perfil(iniciativa)
        API.actualizar_publicaciones(iniciativa)

    with open(os.path.dirname(os.path.dirname(__file__)) + f"/static/iniciativas/biografias.json", "w", encoding='utf-8') as archivo:
        json.dump(biografias, archivo, indent=2)

    return HttpResponse("Iniciativas Actualizadas")


def redireccion(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        fecha_limite = data.get('fechaFormateada') + ".jpg"
        return JsonResponse({'fecha': fecha_limite})
    else:
        return render(request, 'Redireccion.html',{"iniciativas": INICIATIVAS})


def publicaciones(request):
    #Se deben otener siempre las ultimas publicaciones del mes.

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()

    # Calcular la fecha hace 30 días atrás
    fecha_hace_30_dias = fecha_actual - datetime.timedelta(days=30)

    # Formatear la fecha como una cadena personalizada
    formato_fecha = fecha_hace_30_dias.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"

    # Obtener las publicaciones que se han hecho desde hace 30 días
    lista_30 = API.recientes_publicaciones(formato_fecha)

    # Verificar si se ha proporcionado una fecha límite
    fecha_limite = request.GET.get('fecha')
    if fecha_limite is not None:
        lista_custom = API.recientes_publicaciones(fecha_limite)
    else:
        lista_custom = []

    return render(request, 'Publicaciones.html', {"fecha": fecha_limite, "lista_30": lista_30, "lista_custom": lista_custom, "iniciativas": INICIATIVAS})