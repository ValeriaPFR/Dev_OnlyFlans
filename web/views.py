from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {}) 

def indice(request):
    return render(request, 'index.html', {}) #

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})
