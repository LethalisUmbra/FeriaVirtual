from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
# Models
from django.contrib.auth.models import User
from carrito.models import Carrito
from ferias.models import Feria
from .models import Producto
# Forms
from .forms import CreateProductoForm, UpdateProductoForm
from carrito.forms import CreateCarritoForm
from django import forms

# CREATE
@login_required(login_url='/login')
def CreateProducto(request):
	producto_form = CreateProductoForm()
	ferias = Feria.objects.all()
	feriantes = User.objects.filter(id=request.user.id)
	if request.method == "POST" and 'create_btn':
		producto_form = CreateProductoForm(request.POST)
		if producto_form.is_valid():
			producto_form.save()
			messages.success(request, 'Tu producto ha sido creado con éxito')
			return HttpResponseRedirect('/productos/listado')

	context = {
	'form':producto_form,
	'ferias':ferias,
	'feriantes':feriantes
	}

	return render(request, 'productos/create_producto.html',context)

@login_required(login_url='/login')
def ComprarProducto(request, id_producto):
	instance = Carrito()
	instance.producto = Producto.objects.get(id_producto=id_producto).nombre_producto
	instance.precio = Producto.objects.get(id_producto=id_producto).precio_producto
	instance.cliente = request.user.username
	instance.save()
	messages.success(request, 'Tu producto ha sido agregado con éxito al carrito')
	return redirect('homeCarrito')


# READ
@login_required(login_url='/login')
def ListarProductosComprar(request):
	productos = Producto.objects.all().order_by('nombre_producto', 'precio_producto', 'feria', 'feriante')
	return render(request, 'productos/listar_productos_comprar.html', {'productos':productos})

@login_required(login_url='/login')
def ListarProductosPropios(request):
	productos = Producto.objects.filter(feriante=request.user.username).order_by('nombre_producto')
	return render(request, 'productos/listar_productos_propios.html', {'productos':productos})

# UPDATE
@login_required(login_url='/login')
def ModificarProducto(request, id_producto):
	obj = get_object_or_404(Producto, id_producto=id_producto)
	update_form = UpdateProductoForm(request.POST or None, instance=obj)
	if request.method == "POST" and 'update_btn':
		if update_form.is_valid():
			obj=update_form.save(commit = False)
			obj.save()
			messages.success(request, 'Tu producto ha sido modificado con éxito')
			return HttpResponseRedirect('/productos/listado')
	return render(request, 'productos/modificar_producto.html', {'form': update_form, 'producto':obj})

# DELETE
@login_required(login_url='/login')
def DeleteProducto(request, id_producto):
	try:
		p = Producto.objects.get(id_producto= id_producto)
		p.delete()
		messages.success(request, 'Tu producto ha sido eliminado con éxito')
		return HttpResponseRedirect('/productos/listado')
	except Producto.DoesNotExist:
		messages.error(request, 'No se ha encontrado el producto')
		return HttpResponseRedirect('/productos/listado')
	return render(request, 'home.html')