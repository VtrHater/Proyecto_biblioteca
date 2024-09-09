from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #formulario creacion de cuentas de django
from django.contrib.auth.models import User #creacion de usuarios de django
from django.contrib.auth import login, logout, authenticate #poder iniciar y cerrar sesion
from django.http import HttpResponse

def registrar(request):

    if request.method == "GET":
        return render(request, 'base.html',{  
        'forms': UserCreationForm
        })
    else: 
        if request.POST['password1']==request.POST['password2']:  #Confirma que las contraseñas coincidan
            try:
                cuenta= User.objects.create_user(username=request.POST["username"],password=request.POST['password1'])
                cuenta.save()   #si todo es correcto, guarda los datos en la base de datos, genera una cookie para la sesion y 
                login(request, cuenta)  #redirecciona al link con name= "principal"
                return redirect('principal') #Redireccionar sirve tambien entre carpetas del mismo proyecto
            except:
                return render(request, 'base.html',{
                    'forms': UserCreationForm,               #Carga el mismo base.html pero ahora muestra el "error"
                    'error': "Nombre de usuario ya existe"  #que incluimos en la plantilla 
                    })
        else:
            return render(request, 'base.html',{
                'forms': UserCreationForm,
                'error': "Contaseñas no coinciden"
                })

def base(request):
    return render(request, 'home.html') #Funcion para cargar home.html

def cerrar_sesion(request):
    logout(request)
    return redirect ('cerrar_sesion') #Envia al link con el name = cerrar_sesion
     
def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, 'signin.html',{
        'form': AuthenticationForm,
        })
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': "Nombre o contraseña incorrecta"
                })
        else:
            login(request,user)
            return redirect ('principal')



# Create your views here.
