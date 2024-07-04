from django import forms
from .models import Contacto
from .models import Orden

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']

class SeguimientoForm(forms.Form):
    numero_orden = forms.CharField(max_length=10)
    dni = forms.CharField(max_length=8)


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['numero_orden', 'dni', 'estado', 'descripcion', 'fecha_ingreso']
