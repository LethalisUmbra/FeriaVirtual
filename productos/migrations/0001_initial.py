# Generated by Django 3.0.7 on 2020-06-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=150)),
                ('precio_producto', models.IntegerField()),
                ('descripcion_producto', models.TextField(max_length=500)),
                ('imagen_producto', models.ImageField(null=True, upload_to='gallery')),
            ],
        ),
    ]