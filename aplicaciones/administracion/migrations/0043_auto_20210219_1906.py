# Generated by Django 2.2.7 on 2021-02-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0042_pedido_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Enviado', 'Enviado'), ('Entregado', 'Entregado'), ('Recibido', 'Recibido'), ('Devuelto', 'Devuelto')], default='Recibido', max_length=10),
        ),
    ]
