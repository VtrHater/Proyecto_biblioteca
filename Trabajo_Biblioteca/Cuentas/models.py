from django.db import models

# Create your models here.          
class Personal(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=60)

class Solicitudes(models.Model):
    ESTADOS = [
        ('pendiente','Pendiente'),
        ('en_proceso','En proceso'),
        ('completada','Completada'),
        ('rechazada','Rechazada')
    ]
    documento = models.CharField(max_length=100)
    departamento = models.CharField(max_length=60)
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=60)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    


    