from django.urls import path

from. import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('listado_productos',views.list_productos, name='Calculo'),
    path('formulario/',views.formulario, name='formulario'),
    path('respuesta/',views.respuesta, name='respuesta'),


]
      
