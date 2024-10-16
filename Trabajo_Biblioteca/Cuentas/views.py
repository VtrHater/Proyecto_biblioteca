from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import solicitudesform
from .models import Solicitudes, Personal

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
    valor= request.GET
    if request.user.is_authenticated:
        user_name = request.user.username  # Suponiendo que quieres usar el nombre de usuario
        # Filtrar las solicitudes que ha creado el usuario
        # Más adelante se debe hacer la conexión del usuario con el departamento al cual pertenece.
        var_s_usuario = Solicitudes.objects.filter(autor=user_name)
    else:
        var_s_usuario = Solicitudes.objects.none()  # Si no está autenticado, no se muestra nada
    return render(request, 'solicitudes_existentes.html', {'contexto': var_s_usuario,"activas":valor})
    
def editar_mis_solicitudes(request):
    if request.GET:
        return render(request, "editar_mis_solicitudes.html")
        
def editar_personal(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        soli_usuario= Solicitudes.objects.filter(autor=usuario)
    else:
        soli_usuario= Solicitudes.objects.none()
    return render(request,"editar_personales.html", {"valor":soli_usuario})

def editar_solicitud_personal(request, lol):
    if request.method == "GET":
        soli_citud = get_object_or_404(Solicitudes, pk= lol)
        soli_form = solicitudesform(instance = soli_citud)
        return render(request, "editar_solicitudes_personal.html", {"mostrar":soli_citud, "formulario": soli_form})
    else:
        actualizada = get_object_or_404(Solicitudes, pk=lol)
        formulario_actualizado = solicitudesform(request.POST, instance=actualizada)
        formulario_actualizado.save()
        return redirect("filtrar_solicitudes_usuario")
    
def editar_por_departamento(request):
    if request.user.is_authenticated:
        usuario= request.user.id
        department= Personal.objects.values_list("sector").filter(name=usuario)
        department= department[0][0]
        entregar= Solicitudes.objects.filter(departamento=department).values()
        return render(request, "editar_departamental.html",{"mostrar":entregar})