# Generated by Django 2.2.7 on 2022-09-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0059_establecimiento_zonaenvio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Codigo_Usuario',
            fields=[
                ('id_codxusuario', models.AutoField(primary_key=True, serialize=False)),
                ('id_codigo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Codigo')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Usuario')),
            ],
        ),
    ]