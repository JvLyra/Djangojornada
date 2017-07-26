from django.shortcuts import render

from django.http import HttpResponse

from .forms import MatriculaForm , MatriculaModelForm

from .models import Aluno 

# Create your views here.




def home (request):
	parametro = request.GET.get('teste', 'default')
	return HttpResponse('Essa é minha primeira view Django ' + parametro)

def about (request):
		
	form = MatriculaModelForm()
	msg =  None


	if request.method == 'POST':
		form = MatriculaModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = MatriculaModelForm()
			msg = "Cadastro efetuado com sucesso"


	return render(request, 'core/about.html', {'nome': 'joao', 'curso' : 'bussiness', 'disciplinas' : ['ecobrasil','contabilidade','estatistica'], 'form':form,'msg':msg })