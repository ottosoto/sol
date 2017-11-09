# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from muebles.models import Producto, Compra

admin.site.register(Producto)#, ProductoAdmin)
admin.site.register(Compra)#, CompraAdmin)
