# Generated by Django 2.2.7 on 2020-12-06 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0017_auto_20201205_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
