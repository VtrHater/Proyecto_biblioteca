from cProfile import Profile
from collections import UserDict
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Notification

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    dia = timezone.now().strftime('%d-%m-%Y')
    hora = timezone.now().strftime('%H:%M:%S')
    archivo = open("registro.txt", "a")
    archivo.write("{} inicio de sesion el: {} a las: {}".format(user, dia, hora)+"\n")
    archivo.close()

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    dia = timezone.now().strftime('%d-%m-%Y')
    hora = timezone.now().strftime('%H:%M:%S')
    archivo = open("registro.txt", "a")
    archivo.write("{} cierre de sesion el: {} a las: {}".format(user, dia, hora)+"\n")
    archivo.close()

@receiver(post_save, sender=user_logged_in)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=user_logged_in)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender=User)
def notify_on_user_creation(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance,
            message=f"Bienvenido {instance.username}, tu cuenta ha sido creada."
        )