from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registrar(request):
    titulo = "Hola gente"
    return render(request, 'base.html',{
        "titulo": titulo
    })
     



# Create your views here.
