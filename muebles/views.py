from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
#from PROYECTO_APP.forms import EncabezadoForm, MaterialForm
#from PROYECTO_APP.models import Encabezado, Material, Descripcion
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'muebles/index.html')
