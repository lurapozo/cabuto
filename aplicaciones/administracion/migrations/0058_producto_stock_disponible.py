# Generated by Django 2.2.7 on 2022-09-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0057_auto_20220906_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock_disponible',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
    ]