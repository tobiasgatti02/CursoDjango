from . import views
from django.urls import path
app_name = "prueba"

#necesitamos una variable que se llame urlsPatterns

urlpatterns = [
    #primer parametro es la ruta para llamarla
    #segundo parametro es que vista o funcion llamo
    #tercer parametro si en un futuro necesito redireccionar, se redirecciona a index
    path('',views.index, name = "index"),
    path("<str:nombre>",views.saludar, name = "saludar"),
    #<str:nombre> sirve para poner nombre variable en la url y lo salude
   # path('orp',views.index2,name="index")
    #la lectura va por orden de arriba o abajoo los path 
]


#siempre modularizar es mejor para hacer apps grandes, por ejemplo dividir los URLS