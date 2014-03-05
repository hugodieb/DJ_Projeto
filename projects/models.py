#encoding: utf-8

from django.db import models

# Create your models here.

class Project(models.Model):

	name = models.CharField(max_length=100, verbose_name=u'Nome')

	author = models.CharField(max_length=100, verbose_name=u'Autor')

	description = models.TextField(verbose_name=u'Descrição', blank=True)

	Keywords = models.CharField(max_length=255, verbose_name=u'Palavra chave', blank=True)

	slug = models.SlugField(help_text=u'Irá servir para url elegante')

	def __unicode__(self):

		return self.name

	class Meta:

		verbose_name = u'Projeto'
		verbose_name_plural = u'Projetos'
