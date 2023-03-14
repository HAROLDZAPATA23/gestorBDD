from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto={}
    return render(request,'inicio.html', contexto)