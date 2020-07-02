from django import forms
from .models import Feria

class CreateFeriaForm(forms.ModelForm):
	nombre_feria = forms.CharField()
	comuna_feria = forms.CharField()
	inicio_feria = forms.CharField()
	fin_feria = forms.CharField()
	horario_ini_feria = forms.CharField()
	horario_fin_feria = forms.CharField()
	dias_feria = forms.CharField()

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
	nombre_feria = forms.CharField()
	comuna_feria = forms.CharField()
	inicio_feria = forms.CharField()
	fin_feria = forms.CharField()
	horario_ini_feria = forms.CharField()
	horario_fin_feria = forms.CharField()
	dias_feria = forms.CharField()
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