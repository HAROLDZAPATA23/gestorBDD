from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
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
    agnoActual=datetime.now().year
    diaActual=datetime.now().day
    mesActual=datetime.now().month
    agnoNacimiento= int(request.GET["nacimiento"].split('-')[0])
    mesNacimiento=int(request.GET["nacimiento"].split('-')[1])
    diaNacimiento=int(request.GET["nacimiento"].split('-')[2])

    edad=agnoActual - agnoNacimiento
    if mesNacimiento > mesActual:
        edad-=1
    elif mesActual==mesNacimiento:
        if diaActual < diaNacimiento:
            edad-=1


    nombre=request.GET["nombre"]
    genero=request.GET["genero"]
    return render(request,'respu.html',{'nombre':nombre,'edad':edad, 'genero':genero})


