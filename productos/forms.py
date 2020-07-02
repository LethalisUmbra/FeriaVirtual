from django import forms
from .models import Producto

class CreateProductoForm(forms.ModelForm):
	nombre_producto = forms.CharField(min_length=1, max_length=150)
	precio_producto = forms.IntegerField()
	descripcion_producto = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Producto
		fields = [
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