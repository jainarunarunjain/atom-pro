from django import forms
from django.contrib.auth.models import User

class login_form(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
		'username' : forms.TextInput(attrs = {'placeholder': 'Username','required': 'True'}),
		'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','required': 'True'}),
		}

		fields = ['username', 'password']


class signupform(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
		'username' : forms.TextInput(attrs = {'placeholder': 'Username','required': 'True'}),
		'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','required': 'True'}),
		'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','required': 'True'}),

			}
		fields = ['username', 'email', 'password']
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("That Username Is Already Taken")
		return username