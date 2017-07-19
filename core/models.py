from django.db import models

# Create your models here.




class Curso(models.Model):
	nome = models.CharField(max_length=255)
	codigo_geral = models.CharField(max_length=20)
 