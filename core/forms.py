from django import forms 
from .models import Curso 

class MatriculaForm(forms.Form):
	nome = forms.CharField(max_length=100)
	cpf = forms.CharField(max_length=14)
	ranking = forms.DecimalField(max_value=10, min_value=0, decimal_places=2)
	curso = forms.ModelChoiceField(queryset=Curso.objects.all())
	data_de_nascimento = forms.DateField()