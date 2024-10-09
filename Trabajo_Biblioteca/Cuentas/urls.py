from django.urls import path, include
from . import views
from .views import filtrar_activas
from .views import filtrar_solicitudes_usuario

urlpatterns = [

    path('Home/', views.Home, name= "Home"),
    path('crear_cuenta/', views.registrar, name= 'signin'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('solicitudes/', views.solicitud, name ="Solicitudes"),


    path('solicitudes_existentes/',views.soliexistentes, name='soliexistentes'),

    path('solicitudes_lista/', views.solicitudes_lista, name='solicitudes_lista'),

    path('solicitudes_activas/', views.filtrar_activas, name='filtrar_activas'),
    path('mis_solicitudes/', views.filtrar_solicitudes_usuario, name="filtrar_solicitudes_usuario"),
   
   
]
