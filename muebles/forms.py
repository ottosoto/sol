from django import forms
from .models import Compra, Producto

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('fecha', 'usuario', 'productos')

def __init__ (self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields["compras"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["compras"].help_text = "Ingrese los productos"
        self.fields["compras"].queryset = Producto.objects.all()

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('id_categoria', 'id_presentacion_madera', 'nombre','cantidad', 'precio', 'descripcion')
