from django.db import models
from django.contrib.auth.models import User

# Create your models here.          
class Personal(models.Model):
    DEPARTAMENTOS = [
        ("placeholder","Nada"),
        ("Extensión Cultural","Extensión Cultural"),
        ("Servicio de atención a usuarios","Servicio de atención a usuarios"),
        ("Conservación","Conservación"),
        ("Digitalización","Digitalización"),
        ("Depósito Legal","Depósito Legal"),
        ("Adquisiciones Bibliográficas","Adquisiciones Bibliográficas"),
        ("Depósito Legal Electrónico","Depósito Legal Electrónico"),
        ("Mapoteca","Mapoteca"),
        ("Láminas y estampas","Láminas y estampas"),
        ("Fotográfico y audiovisual","Fotográfico y audiovisual"),
        ("Periódicos","Periódicos"),
        ("Hemeroteca","Hemeroteca"),
        ("Fondo General","Fondo General"),
        ("Sección Chilena","Sección Chilena")
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
        ("placeholder","Seleccionar"),
        ("Extensión Cultural","Extensión Cultural"),
        ("Servicio de atención a usuarios","Servicio de atención a usuarios"),
        ("Conservación","Conservación"),
        ("Digitalización","Digitalización"),
        ("Depósito Legal","Depósito Legal"),
        ("Adquisiciones Bibliográficas","Adquisiciones Bibliográficas"),
        ("Depósito Legal Electrónico","Depósito Legal Electrónico"),
        ("Mapoteca","Mapoteca"),
        ("Láminas y estampas","Láminas y estampas"),
        ("Fotográfico y audiovisual","Fotográfico y audiovisual"),
        ("Periódicos","Periódicos"),
        ("Hemeroteca","Hemeroteca"),
        ("Fondo General","Fondo General"),
        ("Sección Chilena","Sección Chilena")
        ]
    Prioridad=[
        ("Muy Importante","Muy Importante"),
        ("Importante","Importante"),
        ("Poco Importante","Poco Importante")
    ]
    documento = models.CharField(max_length=100)
    autor = models.CharField(max_length=60,blank=True)
    fecha_publicación = models.CharField(max_length=20,blank=True)
    número_de_sistema = models.CharField(max_length=20,blank=True)
    ubicación = models.CharField(max_length=20,blank=True)
    departamento = models.CharField(max_length=60, choices=DEPARTAMENTOS,default="placeholder")
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    plazo = models.CharField(max_length=20, blank=True)
    funcionario = models.CharField(max_length=60)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad= models.CharField(max_length=120, choices=Prioridad, default="Importante")

    def __str__(self):
        return f"{self.documento} - {self.autor}"
    
    class Meta:
        ordering = ['-fecha']  # Ordena por fecha de manera ascendente
        ordering = ['departamento']

class Notification (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'

   

    