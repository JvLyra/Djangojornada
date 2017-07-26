from django.db import models

from django.contrib.auth.models import User

# Create your models here.




class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo_geral = models.CharField(max_length=20)

	def __str__(self):
		return '{0} - {1} '.format(self.nome, self.codigo_geral)

class Aluno(models.Model):
	nome =  models.CharField(max_length=255)
	cpf = models.CharField(max_length=14)
	curso = models.ForeignKey(Curso)
	ranking = models.DecimalField(default=0, max_digits=4,decimal_places=2)
	data_de_nascimento = models.DateField()
	user = models.OneToOneField(User)

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.cpf)

class Disciplina(models.Model):
	nome = models.CharField(max_length=255)
	codigo = models.CharField(max_length=20)
	curso = models.ForeignKey(Curso)
	data_de_inserção = models.DateField()
	eh_eletiva = models.BooleanField(default=False)

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.codigo)


