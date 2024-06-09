from django.shortcuts import render
from .models import Usuarios

def index(request):
    return render(request, 'index.html')
    
def iniciarsecion(request):
    return render(request, 'iniciarsecion.html')

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    return render(request, 'registro.html')

def saldo(request):
    return render(request, 'saldo.html')

def tarjeta(request):
    return render(request, 'tarjeta.html')


