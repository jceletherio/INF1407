from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

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
    return render(request, 'mainapp/registro/paginaSecreta.html')

def trocaSenha(request):
    return render(request, 'mainapp/registro/trocaSenha.html')
    
def trocaFeita(request):
    return render(request, 'mainapp/registro/trocaFeita.html')