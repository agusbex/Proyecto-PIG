from django import forms
from django.core.exceptions import ValidationError

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)

class SeguimientoForm(forms.Form):
    numero_orden = forms.IntegerField(label="Número de Orden", required=True)
    dni = forms.IntegerField(label="DNI", required=True)

class AdminLoginForm(forms.Form):
    numero_admin = forms.CharField(label="Administrador", max_length=10, required=True)
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(), required=True)