from django.apps import AppConfig


class CuentasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Cuentas'
    def ready(self):
        
        import Cuentas.signals
        
