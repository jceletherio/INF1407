from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')

def segundaPagina(request):
    return render(request, 'mainapp/segunda.html')
