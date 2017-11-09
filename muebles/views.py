# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.contrib import messages
#from peliculas.models import Pelicula, Actuacion
#from muebles.models import Encabezado, Material, Descripcion
from .forms import CompraForm, ProductoForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'muebles/index.html')

def producto_nuevo(request):
    formulario = ProductoForm()
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
        messages.add_message(request, messages.SUCCESS, 'Producto guardado exitosamente')
    return render(request, 'muebles/producto_nuevo.html', {'formulario': formulario})

def producto_listado(request):
    posts = Producto.objects.filter().order_by('id')
    return render(request, 'muebles/producto_listado.html', {'producto': posts})
