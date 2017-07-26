"""siga2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import HomeView 
from core.views import about
from core.views import LoginView
from core.views import profile
from core.views import logout
from core.views import AlunoDetailView
from core.views import AlunoListView




urlpatterns = [
    url(r'^home$', HomeView.as_view() ),
    url(r'^admin/', admin.site.urls),
    url(r'^about$', about ),
    url(r'^login$', LoginView.as_view() ),
    url(r'^profile$', profile ),
    url(r'^logout$', logout, name='logout' ),
    url(r'^aluno/(?P<pk>\d+)$',AlunoDetailView.as_view(), name='aluno-detail'),
    url(r'^alunos$', AlunoListView.as_view()),


]
