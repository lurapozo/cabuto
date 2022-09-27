# Generated by Django 2.2.7 on 2020-11-07 18:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_establecimiento_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Notificacion',
            fields=[
                ('id_tipxnotificacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id_notificacion', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('id_tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Tipo_Notificacion')),
            ],
        ),
    ]
