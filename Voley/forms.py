from django import forms
from .models import *
from django.forms import  TextInput


class buscadorEquipoForm(forms.Form):
	"""docstring for OrganizacionForm"""
	#class Meta:
	nombre = forms.CharField(label=u'Equipo')
