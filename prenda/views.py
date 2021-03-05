from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from .models import Producto
# Create your views here.


class ProductoView(CreateView,ListView):
	model = Producto
	fields = ['marca','proveedor','industria','color','talle','familia','codigo_barra','descripcion', 'precio', 'stock','iva']
	template_name = 'index.html'
	success_url = '/'
	context_object_name = 'pro'

class ProductoUpdateView(UpdateView):
	model = Producto
	fields = ['marca','proveedor','industria','color','talle','familia','codigo_barra','descripcion', 'precio', 'stock','iva']
	template_name = 'updateForm.html'
	success_url = '/'

class ProductoDeleteView(DeleteView):
	model = Producto
	template_name = 'deleteForm.html'
	success_url = '/'