from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import MatriculaForm , MatriculaModelForm , LoginForm

from .models import Aluno

from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout 

from django.contrib.auth.decorators import login_required 

from django.views.generic import View

from django.views.generic.base import TemplateView

from django.views.generic.detail import DetailView

from django.views.generic.list import ListView



# Create your views here.




def home (request):
	parametro = request.GET.get('teste', 'default')
	return HttpResponse('Essa é minha primeira view Django ' + parametro)


class HomeView(TemplateView):
	template_name = 'core/home.html'

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
@login_required
def profile(request):
	return render(request, 'core/profile.html', {'user':request.user})

def logout(request):
	auth_logout(request)
	return redirect('/about')

def login(request):
	if request.method == 'POST':
		pass 




class LoginView(View):

	def get(self, request):
		form = LoginForm()
		return render(request, 'core/login.html', {'form':form})
	def post(self, request):

		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('email')
			password = form.cleaned_data.get('senha')
			user = authenticate(request, username = username, password = password)
			if user is not None:
				auth_login(request, user)
				return redirect('/profile')
			else:
				msg = 'Email ou senha incorretos'
				return render(request, 'core/login.html', {'form':form, 'msg': msg })


class AlunoDetailView(DetailView):
	model = Aluno
	template_name = 'aluno_detail.html'


class AlunoListView(ListView):
	model = Aluno
	template_name = 'aluno_list.html'