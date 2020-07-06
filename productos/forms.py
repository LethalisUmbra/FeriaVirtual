from django import forms
from .models import Producto
from django.contrib.auth.models import User
from ferias.models import Feria

class CreateProductoForm(forms.ModelForm):
	feria = forms.ModelChoiceField(queryset=Feria.objects.all())
	feriante = forms.ModelChoiceField(queryset=User.objects.all())
	nombre_producto = forms.CharField(min_length=1, max_length=150)
	precio_producto = forms.IntegerField()
	descripcion_producto = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Producto
		fields = [
		"feria",
		"feriante",
		"id_producto",
		"nombre_producto",
		"precio_producto",
		"descripcion_producto"
		]

class UpdateProductoForm(forms.ModelForm):
	nombre_producto = forms.CharField(min_length=1, max_length=150)
	precio_producto = forms.IntegerField()
	descripcion_producto = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Producto
		fields = [
		"nombre_producto",
		"precio_producto",
		"descripcion_producto"
		]