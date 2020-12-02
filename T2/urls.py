"""T2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.urls.base import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('SegundaPagina', views.segundaPagina, name='segunda'),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='mainapp/registro/login.html',), name='sec-login'),
    path('accounts/profile/', views.paginaCandidatos,name='sec-paginaCandidatos'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home'),), name='sec-logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='mainapp/registro/trocaSenha.html', success_url=reverse_lazy('sec-password_change_done'),), name='sec-password_change'),
    path('accounts/password_change_done/', PasswordChangeDoneView.as_view(template_name='mainapp/registro/trocaFeita.html',), name='sec-password_change_done'),
    path('accounts/terminaRegistro/<int:pk>/', UpdateView.as_view( template_name='mainapp/registro/paginaUsuario.html', success_url=reverse_lazy('sec-home'), model=User, fields=['first_name', 'last_name', 'email',],), name='sec-completaDadosUsuario'),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='mainapp/registro/formRecuperacao.html', success_url=reverse_lazy('sec-password_reset_done'), email_template_name='mainapp/registro/paginaRecuperacao.html', subject_template_name='mainapp/registro/password_change_text.txt', from_email='webmaster@meslin.com.br',), name='password_reset'),
    path('accounts/password_reset_done/', PasswordResetDoneView.as_view( template_name='mainapp/registro/recuperacaoFeita.html',), name='sec-password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='mainapp/registro/confSenha.html', success_url=reverse_lazy('sec-password_reset_complete'),), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view(template_name='mainapp/registro/sucessoSenha.html'), name='sec-password_reset_complete'),
    path('accounts/profile/mylist/', views.minhaLista,name='sec-minhaLista'),
    path('accounts/profile/updated/', views.alteraCand,name='sec-alteraCand'),
    path('accounts/profile/update/', views.attCand,name='sec-atualiza'),
    path('accounts/profile/deleta/', views.deleta,name='sec-deleta'),
    path('accounts/profile/excluido/', views.deletaS,name='sec-deletaSucesso'),
    
    
    path('favicon.ico',RedirectView.as_view(url='/static/img/favicon.ico')),
    path('accounts/profile/10',RedirectView.as_view(url='/static/img/10.jpg')),
    path('accounts/profile/12',RedirectView.as_view(url='/static/img/12.jpg')),
    path('accounts/profile/13',RedirectView.as_view(url='/static/img/13.jpeg')),
    path('accounts/profile/25',RedirectView.as_view(url='/static/img/25.jfif')),
    path('accounts/profile/mylist/10',RedirectView.as_view(url='/static/img/10.jpg')),
    path('accounts/profile/mylist/12',RedirectView.as_view(url='/static/img/12.jpg')),
    path('accounts/profile/mylist/13',RedirectView.as_view(url='/static/img/13.jpeg')),
    path('accounts/profile/mylist/25',RedirectView.as_view(url='/static/img/25.jfif')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
