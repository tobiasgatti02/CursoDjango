from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tareas = ["cocinar","lavar","barrer"]
# Create your views here.

class NuevaTareaForm(forms.Form):
    tarea= forms.CharField(label="Tarea")
    prioridad = forms.IntegerField(label="Prioridad",
                                        min_value=1,
                                        max_value=10)

def index(request):
    return render(request, 'tareas/index.html',{
        'tareas':tareas
    })


    
#agregar tarea


def agregar(request):
    if request.method == "POST":
        form = NuevaTareaForm(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            tareas.append(tarea)
            return HttpResponseRedirect(reverse("tareas:index"))
        else:  
            return render(request, "tareas/agregar.html", {
            "form": form})
    else:
        return render(request, "tareas/agregar.html",{
            "form": NuevaTareaForm()
        })
    
    
