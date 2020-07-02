from django.db import models

# Create your models here.

class Feria(models.Model):
	id_feria = models.AutoField(primary_key=True)
	nombre_feria = models.CharField(max_length=150)
	comuna_feria = models.CharField(max_length=150)
	inicio_feria = models.CharField(max_length=200)
	fin_feria = models.CharField(max_length=200)
	horario_ini_feria = models.TimeField()
	horario_fin_feria = models.TimeField()
	dias_feria = models.CharField(max_length=200)

	def __str__(self):
		descripcion = (self.nombre_feria + " " + self.comuna_feria)
		return descripcion