# Generated by Django 3.1.2 on 2024-11-15 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0010_auto_20241115_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitudes',
            old_name='num_sistema',
            new_name='número_de_sistema',
        ),
        migrations.RenameField(
            model_name='solicitudes',
            old_name='ubicacion',
            new_name='ubicación',
        ),
    ]
