#encoding: utf-8

from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):

		#neste metodo posso mudar os campos do formulario com o codigo abaixo#
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['description'].required = True
		self.fields['name'].widget.attrs['placeholder'] = u'Nome do Projeto'

	class Meta:
		model = Project
		#comando abaixo muda campo keyword para um Textarea ao inves do codigo acima por ex.
		#widgets = {
		#	'Keywords': forms.Textarea,
		#}