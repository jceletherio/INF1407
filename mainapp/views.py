from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Mylist, Estado, Municipio, Prefeito
from django.views.generic.base import View
from .forms import mylistForm
from django.urls.base import reverse_lazy


# Create your views here.

class uplistaView(View):
    def get(self, request, *args, **kwargs):
        context = { 'formulario': mylistForm, }
        return render(request,"mainapp/registro/upLista.html", context)

    def post(self, request, *args, **kwargs):
        formulario = mylistForm(request.POST)
        if formulario.is_valid():
            current_user = request.user.username
            ml = Mylist.objects.get(nome=current_user).update(formulario.myprefeito)
            return HttpResponseRedirect(reverse_lazy("sec-alteraCand"))

def home(request):
    return render(request, 'mainapp/home.html')

def segundaPagina(request):
    return render(request, 'mainapp/segunda.html')

def homeSec(request):
    return render(request, 'mainapp/registro/homeSec.html')

def registro(request):
    
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario,}
    return render(request, 'mainapp/registro/registro.html', context)

def login(request):
    return render(request, 'mainapp/registro/login.html')

def paginaSecreta(request):
    current_user = request.user.username
    ml = Mylist.objects.filter(nome=current_user)
    if not ml:
        Mylist.objects.create(nome=current_user, myprefeito=0)
    ls = Estado.objects.get(id=1).municipio_set.get(id=1)
    return render(request, 'mainapp/registro/paginaSecreta.html', {"ls": ls})

def trocaSenha(request):
    return render(request, 'mainapp/registro/trocaSenha.html')
    
def trocaFeita(request):
    return render(request, 'mainapp/registro/trocaFeita.html')

def paginaUsuario(request):
    return render(request, 'mainapp/registro/paginaUsuario.html')

def minhaLista(request):
    current_user = request.user.username
    ml = Mylist.objects.get(nome=current_user).myprefeito
    ls = Estado.objects.get(id=1).municipio_set.get(id=1).prefeito_set.filter(sigla = ml)
    return render(request, 'mainapp/registro/minhaLista.html', {"ls": ls})

def alteraCand(request):
    current_user = request.user.username
    ml = Mylist.objects.get(nome=current_user).update(myprefeito = 25)
    
    return render(request, 'mainapp/registro/alteraCand.html')


