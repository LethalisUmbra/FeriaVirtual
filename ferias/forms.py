from django import forms
from .models import Feria

class CreateFeriaForm(forms.ModelForm):
	nombre_feria = forms.CharField(max_length=150, min_length=4)
	comuna_feria = forms.CharField(max_length=150, min_length=4)
	inicio_feria = forms.CharField(max_length=200, min_length=3)
	fin_feria = forms.CharField(max_length=200, min_length=3)
	horario_ini_feria = forms.TimeField()
	horario_fin_feria = forms.TimeField()
	dias_feria = forms.CharField(max_length=200, min_length=4)

	class Meta:
		model = Feria
		fields = [
		"id_feria",
		"nombre_feria",
		"comuna_feria",
		"inicio_feria",
		"fin_feria",
		"horario_ini_feria",
		"horario_fin_feria",
		"dias_feria"
		]

class UpdateFeriaForm(forms.ModelForm):
	nombre_feria = forms.CharField(max_length=150, min_length=4)
	comuna_feria = forms.CharField(max_length=150, min_length=4)
	inicio_feria = forms.CharField(max_length=200, min_length=3)
	fin_feria = forms.CharField(max_length=200, min_length=3)
	horario_ini_feria = forms.TimeField()
	horario_fin_feria = forms.TimeField()
	dias_feria = forms.CharField(max_length=200, min_length=4)
	class Meta:
		model = Feria
		fields = [
		"nombre_feria",
		"comuna_feria",
		"inicio_feria",
		"fin_feria",
		"horario_ini_feria",
		"horario_fin_feria",
		"dias_feria"
		]