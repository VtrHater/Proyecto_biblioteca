from django.urls import path
from.import views

urlpatterns= [path('principal/', views.principal, name='principal'), 
              path("agregar_solicitudes/", views.agregar_solicitudes, name="agregar_solicitudes")
]
