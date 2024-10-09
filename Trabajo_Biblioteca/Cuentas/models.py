from django.db import models
from django.contrib.auth.models import User

# Create your models here.          
class Personal(models.Model):
    DEPARTAMENTOS = [
        ("placeholder","Nada"),
        ("Matematicas","Matematicas"),
        ("Paleontologia","Paleontologia"),
        ("Restauracion","Restauracion"),
        ("Digitalizacion","Digitalizacion"),
        ("libritos","Libreria"),
        ("Novelas","Novelas"),
        ("cuentos","Cuentos"),
        ]
    name = models.ForeignKey(User, on_delete=models.PROTECT)
    sector = models.CharField(max_length=60, choices=DEPARTAMENTOS,default="placeholder")

    def __str__(self):
        return self.name.username

class Solicitudes(models.Model):
    ESTADOS = [
        ('Pendiente','Pendiente'),
        ('En proceso','En proceso'),
        ('Completada','Completada'),
        ('Rechazada','Rechazada')
    ]
    DEPARTAMENTOS = [
        ("placeholder","Nada"),
        ("Matematicas","Matematicas"),
        ("Paleontologia","Paleontologia"),
        ("Restauracion","Restauracion"),
        ("Digitalizacion","Digitalizacion"),
        ("libritos","Libreria"),
        ("Novelas","Novelas"),
        ("cuentos","Cuentos"),
        ]
    documento = models.CharField(max_length=100)
    departamento = models.CharField(max_length=60, choices=DEPARTAMENTOS,default="placeholder")
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=60)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return self.documento+"- "+self.autor
    


    