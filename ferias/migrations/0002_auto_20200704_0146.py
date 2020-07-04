# Generated by Django 3.0.8 on 2020-07-04 05:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feria',
            name='imagen_feria',
        ),
        migrations.AlterField(
            model_name='feria',
            name='comuna_feria',
            field=models.CharField(max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='feria',
            name='dias_feria',
            field=models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='feria',
            name='fin_feria',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(200), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feria',
            name='horario_fin_feria',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='feria',
            name='horario_ini_feria',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='feria',
            name='inicio_feria',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(200), django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feria',
            name='nombre_feria',
            field=models.CharField(max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
        ),
    ]