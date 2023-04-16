from django.shortcuts import render, redirect
from . import API
from . import forms
from . import models

# Create your views here.

def home(request):
    recientes = API.recientes()
    return render(request,"Home.html",{"key": recientes})

def iniciativa(request, nombre):
    publicaciones = API.contenido(nombre)
    return render(request, f"{nombre}.html", {"key": publicaciones})

def about(request):
    return render(request,"about.html")

def avisos(request):
    lista = models.imagenes_avisos.objects.all().order_by("id").reverse()
    lista.reverse()
    return render(request,"Avisos.html",{"key": lista})

def subir_avisos(request, id=None):
    imagen = forms.avisos_forms(request.POST, request.FILES)

    if request.method == "POST":
        if imagen.is_valid():
            imagen.save()
            return redirect(avisos)
    context = {"imagen": imagen}
    return render(request, 'Subir_Avisos.html', context)

def test(request):
    API.actualizar_2()
    lista = API.recientes()
    return render(request,"Home.html",{"key": lista})

