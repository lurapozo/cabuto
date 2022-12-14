# Generated by Django 2.2.7 on 2022-09-06 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0056_establecimiento_referencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardauth',
            fields=[
                ('id_cardauth', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=20)),
                ('auth', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='notificacion',
            name='id_establecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]
