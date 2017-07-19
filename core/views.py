from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.




def home (request):
	return HttpResponse("Essa é minha primeira view Django")

def about (request):

	return render(request, 'core/about.html', {'nome': 'joao', 'curso' : 'bussiness', 'disciplinas' : ['ecobrasil','contabilidade','estatistica']  })