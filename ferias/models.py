from django.db import models
from django.core.validators import *

# Create your models here.

class Feria(models.Model):
	id_feria = models.AutoField(primary_key=True)
	nombre_feria = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	comuna_feria = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	inicio_feria = models.CharField(max_length=200, validators=[MaxLengthValidator(200), MinLengthValidator(3)])
	fin_feria = models.CharField(max_length=200, validators=[MaxLengthValidator(200), MinLengthValidator(3)])
	horario_ini_feria = models.TimeField()
	horario_fin_feria = models.TimeField()
	dias_feria = models.CharField(max_length=50, validators=[MaxLengthValidator(50), MinLengthValidator(4)])

	def __str__(self):
		descripcion = (self.nombre_feria + " " + self.comuna_feria)
		return descripcion