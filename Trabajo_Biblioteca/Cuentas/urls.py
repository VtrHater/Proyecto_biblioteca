from django.urls import path
from . import views

urlpatterns = [
    path('Testing/', views.base, name = 'Testeo'),  #Propenso a cambiar, de momento es solo para testear las funcionalidades
    path('signup/', views.registrar, name="signup"), #carga el formulario de creacion de cuentas
    path('signout/', views.cerrar_sesion, name ="Cerrar"), #se encargara del apartado de cerrar sesion
]