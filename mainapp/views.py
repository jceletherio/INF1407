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
from django.contrib.auth import get_user_model


# Create your views here.
def attCand(request):
    if request.method == "POST":
        form = mylistForm(request.POST)
        if form.is_valid():
            current_user = request.user.username
            ml = Mylist.objects.get(nome=current_user)
            ml.myprefeito = form.cleaned_data['myprefeito']
            ml.save()
            return HttpResponseRedirect(reverse_lazy("sec-alteraCand"))
    else:
        form = mylistForm()
    return render(request, 'mainapp/registro/upLista.html', {'form': form})

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

def paginaCandidatos(request):
    current_user = request.user.username
    ml = Mylist.objects.filter(nome=current_user)
    if not ml:
        Mylist.objects.create(nome=current_user, myprefeito=0)
    ls = Estado.objects.get(id=1).municipio_set.get(id=1)
    return render(request, 'mainapp/registro/paginaCandidatos.html', {"ls": ls})

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
    if not ls:
        pass
    else:
        ls = Estado.objects.get(id=1).municipio_set.get(id=1).prefeito_set.get(sigla = ml)
    return render(request, 'mainapp/registro/minhaLista.html', {"ls": ls})

def alteraCand(request):    
    return render(request, 'mainapp/registro/alteraCand.html')

def deleta(request):
    return render(request, 'mainapp/registro/deleta.html')

def deletaS(request):
    current_user = request.user.username
    Mylist.objects.get(nome=current_user).delete()
    User = get_user_model()
    User.objects.get(username = current_user).delete()
    return render(request, 'mainapp/registro/excluido.html')
