# Generated by Django 2.2.7 on 2021-04-02 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0052_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_Nac',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='foto',
        ),
    ]
