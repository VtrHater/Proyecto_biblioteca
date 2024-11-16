# Generated by Django 3.1.2 on 2024-11-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0005_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitudes',
            old_name='autor',
            new_name='funcionario',
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='sector',
            field=models.CharField(choices=[('placeholder', 'Nada'), ('Matematicas', 'Matematicas'), ('Paleontologia', 'Paleontologia'), ('Restauracion', 'Restauracion'), ('Digitalizacion', 'Digitalizacion'), ('libritos', 'Libreria'), ('Novelas', 'Novelas'), ('Cuentos', 'Cuentos')], default='placeholder', max_length=60),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]