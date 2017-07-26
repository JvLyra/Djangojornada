from django import forms 
from .models import Curso, Aluno 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MatriculaForm(forms.Form):
	nome = forms.CharField(max_length=100)
	cpf = forms.CharField(max_length=14)
	ranking = forms.DecimalField(max_value=10, min_value=0, decimal_places=2)
	curso = forms.ModelChoiceField(queryset=Curso.objects.all())
	data_de_nascimento = forms.DateField()

	def save(self):
		data = self.cleaned_data
		novo_aluno = Aluno(**data)
		novo_aluno.save()
		return novo_aluno


class MatriculaModelForm(forms.ModelForm):
	email = forms.EmailField()
	senha = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = Aluno
		fields = ['nome', 'cpf','curso','data_de_nascimento','email','senha']

	def clean(self):
		data = super(MatriculaModelForm, self).clean()

		if User.objects.filter(username= data.get('email')).count() > 0:
			raise ValidationError("Username ja usado", code = 'invalid_username')
		
		user = User.objects.create_user(data.get('email'),data.get('email'),data.get('senha'))
		data['user'] = user
		return data 




	def save(self, *args, **kwargs):
		self.instance.user = self.cleaned_data.get('user')
		self.instance.ranking = 5
		return super(MatriculaModelForm, self).save()


class LoginForm(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())




