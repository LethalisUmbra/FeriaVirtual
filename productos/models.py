from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	nombre_producto = models.CharField(max_length=150)
	precio_producto = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
	descripcion_producto = models.TextField(max_length=500)

	def __str__(self):
		return self.nombre_producto