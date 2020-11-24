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
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from django.urls.base import reverse_lazy
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('SegundaPagina', views.segundaPagina, name='segunda'),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='mainapp/registro/login.html',), name='sec-login'),
    path('accounts/profile/', views.paginaSecreta,name='sec-paginaSecreta'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home'),), name='sec-logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='mainapp/registro/trocaSenha.html', success_url=reverse_lazy('sec-password_change_done'),), name='sec-password_change'),
    path('accounts/password_change_done/', PasswordChangeDoneView.as_view(template_name='mainapp/registro/trocaFeita.html',), name='sec-password_change_done'),

    path('accounts/', include('django.contrib.auth.urls')),
    
]
