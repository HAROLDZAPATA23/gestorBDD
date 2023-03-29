from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    contexto={}
    return render(request,'inicio.html', contexto)

def list_productos(request):
    productos=['Portatil lenovo','Iphone galaxiA35','Rolex titan','Motog7']
    contexto={ 'listado':productos}
    return render(request,'list_productos.html', contexto)

def formulario(request):
    return render(request,'formulario.html')

def respuesta(request):

    nombre=request.GET["nombre"]
    nacimiento=request.GET["nacimiento"]
    genero=request.GET["genero"]
    mensaje="Hola %r Biembenido, tu fecha de nacimiento es %r ,  y tu genero es %r " %(nombre, nacimiento, genero)

    return HttpResponse(mensaje)
