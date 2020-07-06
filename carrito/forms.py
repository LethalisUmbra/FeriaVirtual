from django import forms
from .models import Carrito
from django.contrib.auth.models import User

class CreateCarritoForm(forms.ModelForm):
	producto = forms.CharField(min_length=4, max_length=150)
	precio = forms.IntegerField()
	cliente = forms.CharField(min_length=5, max_length=150)

	class Meta:
		model = Carrito
		fields = [
		"id_carrito",
		"producto",
		"precio",
		"cliente",
		]

class UpdateCarritoForm(forms.ModelForm):
	producto = forms.CharField(min_length=4, max_length=150)
	precio = forms.IntegerField()

	class Meta:
		model = Carrito
		fields = [
		"producto",
		"precio"
		]