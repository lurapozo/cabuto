# Generated by Django 2.2.7 on 2020-12-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0018_auto_20201206_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_oferta',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
