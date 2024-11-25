from django.urls import path, include
from . import views
from .views import editar_perfil, filtrar_activas
from .views import filtrar_solicitudes_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.Home, name= "Home"),
    path('crear_cuenta/', views.registrar, name= 'signin'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('solicitudes/', views.solicitud, name ="Solicitudes"),
    path('solicitudes_existentes/',views.soliexistentes, name='soliexistentes'),
    path('solicitudes_lista/', views.solicitudes_lista, name='solicitudes_lista'),
    path('solicitudes_activas/', views.filtrar_activas, name='filtrar_activas'),
    path('mis_solicitudes/', views.filtrar_solicitudes_usuario, name="filtrar_solicitudes_usuario"),
    path('mis_solicitudes/editar_solicitud/', views.editar_mis_solicitudes, name="Edit"),
    path("editar_personales/", views.editar_personal, name= "Editar_Personales"),
    path("editar_personales/<int:lol>", views.editar_solicitud_personal, name="editar_solicitud_personal"),
    path("editar_departamental/", views.editar_departamento, name= "filtrar_solicitudes_usuario_estados"),
    path("editar_estados/<int:lol>", views.editar_estados, name="editar_estados"),
    path("solicitudes_existentes/prioridades", views.prioridades, name="Prioridad"),
    path('administrador/', views.administrador, name='administrador'),
    path("descargar/", views.descargar, name='descargar'),
    path('perfil/', views.profile_view, name='perfil'),
    path('redireccion_solicitudes/', views.redirigir_solicitudes, name='redirigir_solicitudes'),
    path('prioridades_usuario/', views.prioridades_usuario, name='prioridades_usuario'),
    path('solicitudes_dep/', views.soli_dep , name='solicitudes_dep'),
    path("perfil/editar/", view=editar_perfil, name="editar_perfil"),
    path('enviar_notificacion/', views.enviar_notificacion, name='enviar_notificacion'),
    path('reporte/', views.ReportePersonalizadoExcel.as_view(), name = 'reporte'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

