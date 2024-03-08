from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"prueba/index.html")

def saludar(request, nombre):
    return render(request, "prueba/saludar.html", {
        "nombre": nombre
    })
