#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):

	user = models.ForeignKey(User)	
	name = models.CharField(max_length=100, verbose_name=u'Nome')
	author = models.CharField(max_length=100, verbose_name=u'Autor')
	description = models.TextField(verbose_name=u'Descrição', blank=True)
	
	@classmethod
	def infoProject(cls, user, name, author, description):
		project = cls()
		project.user = user
		project.name = name
		project.author = author
		project.description = description

		return project

class Person(models.Model):

	user = models.ForeignKey(User)
	username = models.CharField(max_length=100, verbose_name=u'Nome')
	usermail = models.EmailField(max_length=256, verbose_name=u'Email')

	@classmethod
	def infoPerson(cls, user):
		person = cls()
		person.user = user
		person.username = user.username
		person.usermail = user.usermail



