# Generated by Django 2.2.7 on 2021-01-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0035_cupones'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='estado',
            field=models.CharField(default='NOT', max_length=500),
        ),
    ]
