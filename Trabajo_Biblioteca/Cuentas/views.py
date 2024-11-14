from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Notification
from .forms import solicitudesform,estadosSolicitudesform
from .models import Solicitudes, Personal
import mimetypes
import os
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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
    if 'activas' in request.GET and request.GET['activas'] == 'true':
        var_activas = Solicitudes.objects.exclude(estado='Completada')
    else:
        var_activas = Solicitudes.objects.all()
    return render(request, 'solicitudes_activas.html', {'contexto': var_activas})

def filtrar_solicitudes_usuario(request):
    valor= request.GET
    if request.user.is_authenticated:
        user_name = request.user.username 
        departamento = valor.get('departamento') 
        if departamento and departamento != "placeholder":
            var_s_usuario = var_s_usuario.filter(departamento=departamento)
        var_s_usuario = Solicitudes.objects.filter(autor=user_name)
    else:
        var_s_usuario = Solicitudes.objects.none()
    return render(request, 'mis_solicitudes.html', {'contexto': var_s_usuario,"activas":valor})


def editar_mis_solicitudes(request):
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
    
def editar_departamento(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        soli_usuario= Solicitudes.objects.filter(autor=usuario)
    else:
        soli_usuario= Solicitudes.objects.none()
    return render(request,"editar_solicitud_departamento.html", {"valor":soli_usuario})


def editar_estados(request, lol):
    if request.method == "GET":
        soli_citud = get_object_or_404(Solicitudes, pk= lol)
        soli_form = estadosSolicitudesform(instance = soli_citud)
        return render(request, "editar_solicitudes_personal.html", {"mostrar":soli_citud, "formulario": soli_form})
    else:
        actualizada = get_object_or_404(Solicitudes, pk=lol)
        formulario_actualizado = estadosSolicitudesform(request.POST, instance=actualizada)
        formulario_actualizado.save()
        return redirect("filtrar_solicitudes_usuario_estados")
    
    
def filtrar_solicitudes_usuario_estados(request):
    valor= request.GET
    if request.user.is_authenticated:
        user_name = request.user.username  
        departamento = valor.get('departamento') 
        if departamento and departamento != "placeholder":
            var_s_usuario = var_s_usuario.filter(departamento=departamento)
        var_s_usuario = Solicitudes.objects.filter(autor=user_name)
    else:
        var_s_usuario = Solicitudes.objects.none()  
    return render(request, 'editar_departamento.html', {'contexto': var_s_usuario,"activas":valor})
    
def prioridades(request):
    soli_MI= Solicitudes.objects.filter(prioridad="Muy Importante")
    soli_I= Solicitudes.objects.filter(prioridad="Importante")
    soli_PI= Solicitudes.objects.filter(prioridad="Poco Importante")
    return render(request,"prioridad.html", {
        "MI":soli_MI,
        "I":soli_I,
        "PI":soli_PI
    })

def prioridades_usuario(request):
    if request.user.is_authenticated:
        usuario = request.user.id  
        department = Personal.objects.filter(name=usuario).values_list("sector", flat=True).first()
        if department is None:
            department = "placeholder"  
        soli_MI = Solicitudes.objects.filter(prioridad="Muy Importante", departamento=department)
        soli_I = Solicitudes.objects.filter(prioridad="Importante", departamento=department)
        soli_PI = Solicitudes.objects.filter(prioridad="Poco Importante", departamento=department)
        
        return render(request, "prioridad_usuario.html", {
            "MI": soli_MI,
            "I": soli_I,
            "PI": soli_PI
        })

def administrador(request):
    return render(request, "administrador.html")

def descargar(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nom_archivo = "registro.txt"
    filepath = BASE_DIR + "\\" + nom_archivo
    path = open(filepath, "r")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type = mime_type)
    response["content_disposition"] = "attachment; nombre={}".format(nom_archivo)
    return response

def profile_view(request):
    notifications = []
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user)
    return render(request, 'cuentas/profile.html', {'notifications': notifications})

@login_required
def redirigir_solicitudes(request):
    if request.user.groups.filter(name='Usuarios_jefes').exists():
        return redirect('soliexistentes')  
    elif request.user.groups.filter(name='Usuarios_general').exists():
        return redirect('filtrar_solicitudes_usuario') 
    else:
        return redirect('Home')  
    
def soli_dep(request):
    return render(request, 'solicitudes_dep.html')
