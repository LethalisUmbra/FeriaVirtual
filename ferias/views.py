from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .forms import CreateFeriaForm, UpdateFeriaForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Feria

# CREATE
@login_required(login_url='/login')
def CreateFeria(request):
	feria_form = CreateFeriaForm()

	if request.method == "POST" and 'create_btn':
		feria_form = CreateFeriaForm(request.POST)
		if feria_form.is_valid():
			feria_form.save()
			messages.success(request, 'Tu feria ha sido creada con éxito')
			return HttpResponseRedirect('/ferias/listado')
		else:
		    messages.error(request, 'No se ha podido crear la feria')
	return render(request, 'ferias/create_feria.html',{'feria_form':feria_form})

# READ
@login_required(login_url='/login')
def ListarFerias(request):
	ferias = Feria.objects.all().order_by('nombre_feria')

	return render(request, 'ferias/listar_ferias.html', {'ferias':ferias})

# UPDATE
@login_required(login_url='/login')
def ModificarFeria(request, id_feria):
	obj = get_object_or_404(Feria, id_feria=id_feria)
	update_form = UpdateFeriaForm(request.POST or None, instance=obj)
	if request.method == "POST" and 'update_btn':
		if update_form.is_valid():
			obj=update_form.save(commit = False)
			obj.save()
			messages.success(request, 'Tu feria ha sido modificada con éxito')
			return HttpResponseRedirect('/ferias/listado')
	return render(request, 'ferias/modificar_feria.html', {'form': update_form, 'feria':obj})

# DELETE
@login_required(login_url='/login')
def DeleteFeria(request, id_feria):
	try:
		f = Feria.objects.get(id_feria= id_feria)
		f.delete()
		messages.success(request, 'La feria ha sido eliminada con éxito')
		return HttpResponseRedirect('/ferias/listado')
	except Feria.DoesNotExist:
		return render(request, 'home.html')
	return render(request, 'home.html')