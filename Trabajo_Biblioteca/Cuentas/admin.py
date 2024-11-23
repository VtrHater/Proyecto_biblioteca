from django.contrib import admin
from .models import Notification, Solicitudes, Personal
# Register your models here.

admin.site.register(Solicitudes)
admin.site.register(Personal)
admin.site.register(Notification)