from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import solicitudesform
from .models import Solicitudes

def registrar(request):
    if request.method == "GET":
        return render(request, "base.html",{
        "form": UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("Solicitudes")
            except: 
                return render(request, "base.html",{
                "form": UserCreationForm,
                'error': "Nombre de usuario en uso"
                }) 
        else:
            return render(request, "base.html",{
                "form": UserCreationForm,
                'error': "Contraseñas no coinciden"
                }) 

def tareas(request):
    return render(request, "solicitudes.html")

def Home(request):
    return render(request, 'Home.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html',{
            'form': AuthenticationForm,
            'error': "Nombre de cuenta o contraseña incorrectos"
            })
        else:
            login(request,user)
            return redirect('Home')
def solicitud(request):
    data = {
        'form': solicitudesform()
    }

    if request.method == 'POST':
        formulario = solicitudesform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "solicitud enviada"
        else:
            data["form"] = formulario

    return render(request, 'solicitudes.html', data)



def soliexistentes(request):
    variable = Solicitudes.objects.values() #values. variable es la info.
    return render(request, 'solicitudes_existentes.html', {'contexto': variable})

def solicitudes_lista(request):
    variable = Solicitudes.objects.all() #all
    return render(request,'solicitudes_existentes.html', {'contexto': variable})


def filtrar_activas(request):
    # Si el parámetro 'activas' está en la URL y es 'true'
    if 'activas' in request.GET and request.GET['activas'] == 'true':
        # Filtrar las solicitudes que no están en estado 'completada'
        var_activas = Solicitudes.objects.exclude(estado='completada')
    else:
        # Mostrar todas las solicitudes si el parámetro no está presente
        var_activas = Solicitudes.objects.all()

    # Renderizar la plantilla con el contexto de las solicitudes filtradas
    return render(request, 'solicitudes_existentes.html', {'contexto': var_activas})

def filtrar_solicitudes_usuario(request):
    if request.user.is_authenticated:
        user_name = request.user.username  # Suponiendo que quieres usar el nombre de usuario
        # Filtrar las solicitudes que ha creado el usuario
        # Más adelante se debe hacer la conexión del usuario con el departamento al cual pertenece.
        var_s_usuario = Solicitudes.objects.filter(autor=user_name)
    else:
        var_s_usuario = Solicitudes.objects.none()  # Si no está autenticado, no se muestra nada
    return render(request, 'solicitudes_existentes.html', {'contexto': var_s_usuario})
    
    
