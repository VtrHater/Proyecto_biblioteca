# Generated by Django 3.1.2 on 2024-11-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0008_auto_20241115_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudes',
            name='autor',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='num_sistema',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='ubicación',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]