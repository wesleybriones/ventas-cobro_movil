from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Vendedor, Usuario
from django import template

# Create your views here.
def vendedor(request):
  vendedors = Usuario.objects.filter(idrol=1)
  context = {'vendedores':vendedors}
  return render(request, 'usuarios/vendedor.html', context) 

def index(request):
  return render(request, 'cuentas/login.html')