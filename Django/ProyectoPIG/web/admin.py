from django.contrib import admin
from .models import Contacto, Orden

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha')

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'dni', 'estado', 'fecha_ingreso')
