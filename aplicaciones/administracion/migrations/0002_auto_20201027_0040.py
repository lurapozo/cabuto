# Generated by Django 2.2.7 on 2020-10-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='cliente', max_length=100),
        ),
    ]
