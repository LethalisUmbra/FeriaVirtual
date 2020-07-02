from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic

# Formulario y Autenticación del Usuario
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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
			messages.error(request, 'Error')

	return render(request, 'login.html', {'form':login_form})