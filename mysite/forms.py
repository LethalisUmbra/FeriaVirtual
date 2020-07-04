from django import forms
from django.contrib.auth.models import User

class UpdateUser(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = [
		"first_name",
		"last_name",
		"email"
		]