from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProductoForm, UpdateProductoForm
from django.http import HttpResponseRedirect
from .models import Producto

# CREATE
@login_required(login_url='/login')
def CreateProducto(request):
	producto_form = CreateProductoForm()

	if request.method == "POST" and 'create_btn':
		producto_form = CreateProductoForm(request.POST)
		if producto_form.is_valid():
			producto_form.save();
			return HttpResponseRedirect('/productos/listado')

	return render(request, 'productos/create_producto.html',{'form':producto_form})

# READ
@login_required(login_url='/login')
def ListarProductos(request):
	productos = Producto.objects.all().order_by('nombre_producto')

	return render(request, 'productos/listar_productos.html', {'productos':productos})

# UPDATE
@login_required(login_url='/login')
def ModificarProducto(request, id_producto):
	obj = get_object_or_404(Producto, id_producto=id_producto)
	update_form = UpdateProductoForm(request.POST or None, instance=obj)
	if request.method == "POST" and 'update_btn':
		if update_form.is_valid():
			obj=update_form.save(commit = False)
			obj.save()
			return HttpResponseRedirect('/productos/listado')
	return render(request, 'productos/modificar_producto.html', {'form': update_form, 'producto':obj})

# DELETE
@login_required(login_url='/login')
def DeleteProducto(request, id_producto):
	try:
		p = Producto.objects.get(id_producto= id_producto)
		p.delete()
		return HttpResponseRedirect('/productos/listado')
	except Producto.DoesNotExist:
		return render(request, 'home.html')
	return render(request, 'home.html')