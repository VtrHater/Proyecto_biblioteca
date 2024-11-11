from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    dia = timezone.now().strftime('%d-%m-%Y')
    hora = timezone.now().strftime('%H:%M:%S')
    archivo = open("registro.txt", "a")
    archivo.write("{} inicio sesion el: {} a las: {}".format(user, dia, hora)+"\n")
    archivo.close()

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    dia = timezone.now().strftime('%d-%m-%Y')
    hora = timezone.now().strftime('%H:%M:%S')
    archivo = open("registro.txt", "a")
    archivo.write("{} carro sesion el: {} a las: {}".format(user, dia, hora)+"\n")
    archivo.close()