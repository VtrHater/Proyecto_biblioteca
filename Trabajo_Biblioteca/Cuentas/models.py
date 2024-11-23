from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django import forms
import os

def user_image_upload_to(instance, filename):
    # Obtiene la extensión del archivo
    ext = filename.split('.')[-1]
    filename='ll'
    # Define la ruta del archivo a almacenar
    upload_path = os.path.join('user_images', f'{instance.user.username}_image.{ext}')
    
    # Crea el directorio si no existe
    directory = os.path.dirname(upload_path)
  

    try:
        # Si deseas eliminar todos los archivos, pero solo los archivos relacionados con el usuario
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            # Elimina solo los archivos de imagen (que corresponden al usuario)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files in directory {directory}: {e}")
    
    return upload_path

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.user}: {self.message}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.ImageField(upload_to=user_image_upload_to)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambia el nombre aquí
        blank=True,
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Cambia el nombre aquí
        blank=True,
        help_text='Specific permissions for this user.',
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'department', 'profile_image']
        class Meta: 
            swappable = 'AUTH_USER_MODEL'
   

    