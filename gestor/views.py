from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto={}
    return render(request,'inicio.html', contexto)

def list_productos(request):
    productos=['Portatil lenovo','Iphone galaxiA35','Rolex titan','Motog7']
    contexto={ 'listado':productos}
    return render(request,'list_productos.html', contexto)