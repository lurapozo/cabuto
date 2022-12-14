# Generated by Django 2.2.7 on 2020-10-26 23:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('tiene_combo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id_combo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='')),
                ('precio_total', models.FloatField()),
                ('estado', models.CharField(max_length=100)),
                ('cantidad_disponible', models.IntegerField()),
                ('cantidad_despachada', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('razon_social', models.CharField(max_length=300)),
                ('ruc_cedula', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id_establecimiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('encargado', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='NULL', max_length=100)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('estado', models.CharField(max_length=1)),
                ('id_categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Politica',
            fields=[
                ('id_politica', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('detalle', models.CharField(max_length=2000)),
                ('fecha', models.DateField()),
                ('id_empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento_Producto',
            fields=[
                ('id_estabxprod', models.AutoField(primary_key=True, serialize=False)),
                ('stock_disponible', models.IntegerField()),
                ('stock_despacho', models.IntegerField()),
                ('id_establecimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Carrito',
            fields=[
                ('id_detallexcarrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('id_carrito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Carrito')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Combo_Producto',
            fields=[
                ('id_comboxproducto', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_combo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Combo')),
                ('id_establecimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='combo',
            name='id_establecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('metodo_pago', models.CharField(default='Efectivo', max_length=100)),
                ('telefono', models.CharField(default='NONE', max_length=100)),
                ('direccion', models.CharField(default='NONE', max_length=100)),
                ('fecha_Nac', models.DateField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='id_establecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Cliente'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='id_combo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Combo'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='id_establecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Establecimiento'),
        ),
    ]
