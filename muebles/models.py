from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.
#ACTOR      = Producto
#PELICULA   = Compra
#ACTUACION  = Detalle
class Producto(models.Model):
    id_categoria = models.CharField(max_length=30)
    id_presentacion_madera = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=6)
    precio = models.CharField(max_length=30)
    descripcion=models.CharField(max_length=60)
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField()
    usuario = models.CharField(max_length=60)
    productos = models.ManyToManyField(Producto, through='Detalle')
    def __str__(self):
        return self.usuario

class Detalle (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)


class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1

class MaterialAdmin(admin.ModelAdmin):
    inlines = (DetalleInLine,)

class EncabezadoAdmin (admin.ModelAdmin):
    inlines = (DetalleInLine,)
