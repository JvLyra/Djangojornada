from django.shortcuts import render

from django.http import HttpResponse

from .forms import MatriculaForm

# Create your views here.




def home (request):
	parametro = request.GET.get('teste', 'default')
	return HttpResponse("Essa é minha primeira view Django "+parametro)

def about (request):
	form = MatriculaForm()

	
	return render(request, 'core/about.html', {'nome': 'joao', 'curso' : 'bussiness', 'disciplinas' : ['ecobrasil','contabilidade','estatistica'], 'form':form })