from django.urls import path
from . import views

urlpatterns = [
    path('crear_cuenta/', views.registrar, name= 'signin'),
    path('solicitudes/', views.solicitud, name ="Solicitudes"),
    path('Home/', views.Home, name= "Home"),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion')
]