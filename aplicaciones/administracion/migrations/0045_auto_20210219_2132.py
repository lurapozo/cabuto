# Generated by Django 2.2.7 on 2021-02-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0044_calificacionpedido_transaccionpedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccionpedido',
            name='transaccion',
            field=models.CharField(max_length=100),
        ),
    ]
