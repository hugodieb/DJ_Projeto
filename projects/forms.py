#encoding: utf-8

from django import forms
from django.contrib.auth.models import User 

from .models import Project

#class ProjectForm(forms.ModelForm):


		#def __init__(self, *args, **kwargs):

		#neste metodo posso mudar os campos do formulario com o codigo abaixo#
	#	super(ProjectForm, self).__init__(*args, **kwargs)
	#	self.fields['description'].required = True
	#	self.fields['name'].widget.attrs['placeholder'] = u'Nome do Projeto'

	#class Meta:
	#	model = Project
		#comando abaixo muda campo keyword para um Textarea ao inves do codigo acima por ex.
		#widgets = {
		#	'Keywords': forms.Textarea,
		#}

class PersonForm(forms.Form):

	username = forms.CharField(label='Nome', widget=forms.TextInput())
	usermail = forms.EmailField(label=u'Email', widget=forms.TextInput())


class LoginForm(forms.Form):
	username = forms.CharField(label="Usuário",widget=forms.TextInput())
	password = forms.CharField(label="Senha",widget=forms.PasswordInput(render_value=False))


class RegisterForm(forms.Form):
	username = forms.CharField(label="Nome de Usuário",widget=forms.TextInput())
	email = forms.EmailField(label="Email", widget=forms.TextInput())
	password_one = forms.CharField(label="Senha", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput(render_value=False))

	#verificação e pesquisa de usuario ja cadastrado
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nome de usuário já existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email já cadastrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']

		if password_one == password_two:
			pass

		else:
			raise forms.ValidationError('Senhas não conferem')