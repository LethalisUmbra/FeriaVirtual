from django.db import models
from django.conf import settings
from django.core.validators import *
from ferias.models import Feria

# Create your models here.

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	feria = models.ForeignKey(Feria, on_delete=models.CASCADE, null=True)
	feriante = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	nombre_producto = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	precio_producto = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
	descripcion_producto = models.TextField(max_length=500, validators=[MaxLengthValidator(500), MinLengthValidator(5)])

	def __str__(self):
		return self.nombre_producto
