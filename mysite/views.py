from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic

# Formulario y Autenticación del Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import UpdateUser

@login_required(login_url='/login')
def home(request):
	return render(request, 'home.html',{})

def login(request):
	# codigo para el formulario del login con autenticación
	login_form = AuthenticationForm()
	if request.method == "POST" and 'login_btn':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				return redirect('home')
		else:
			messages.error(request, 'No se ha podido iniciar sesión')

	return render(request, 'login.html', {'form':login_form})

@login_required(login_url='/login')
def profile(request, username):
	login(request)
	obj= get_object_or_404(User, username=username)
	update_form = UpdateUser(request.POST or None, instance=obj)
	if request.method == "POST" and 'update_btn':
		if update_form.is_valid():
			obj=update_form.save(commit = False)
			obj.save()
			return	render(request, 'profile.html', {'update': update_form})

	return render(request, 'profile.html', {'update': update_form})

@login_required(login_url='/login')
def deleteUser(request, username):
	try:
		u = User.objects.get(username= username)
		u.delete()
		return redirect('login')
	except User.DoesNotExist:
		return redirect('login')
	return redirect('login')