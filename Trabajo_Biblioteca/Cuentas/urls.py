from django.urls import path, include
from . import views

urlpatterns = [
   
    path('Home/', views.Home, name= "Home"),
    path('crear_cuenta/', views.registrar, name= 'signin'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('solicitudes/', views.solicitud, name ="Solicitudes"),


    path('solicitudes_existentes/',views.soliexistentes, name='soliexistentes'),

    path('Solicitudes/', views.solicitudes_lista, name='solicitudes_lista')
   
   
]
