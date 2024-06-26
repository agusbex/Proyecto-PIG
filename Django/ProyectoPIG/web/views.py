from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    
    context = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now()
    }
    
    return render(request, 'web/index.html', context)
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            print("Datos del formulario de contacto:")
            print(form.cleaned_data)
            
            messages.success(request, 'Tu consulta ha sido enviada con éxito')
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'web/contacto.html', {'form': form})

def seguimiento(request):
    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            numero_orden = form.cleaned_data['numero_orden']
            dni = form.cleaned_data['dni']
            #orden de simulacion
            orden = {
                'numero_orden': numero_orden,
                'dni': dni,
                'estado': 'En progreso',
                'descripcion': 'Reparación de pantalla',
                'fecha_ingreso': '2024-05-20'
            }
            return render(request, 'web/detalle_orden.html', {'orden': orden})
    else:
        form = SeguimientoForm()
    return render(request, 'web/seguimiento.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            numero_admin = form.cleaned_data['numero_admin']
            contraseña = form.cleaned_data['contraseña']
            #simula validacion de administrador
            if numero_admin == 'admin' and contraseña == 'admin123':
                return redirect('administracion')
            else:
                messages.error(request, 'Credenciales de administrador inválidas')
    else:
        form = AdminLoginForm()
    return render(request, 'web/admin_login.html', {'form': form})

def administracion(request):
    #con BBDD va a ser agregar, modificar o eliminar ordenes
    contexto = {
        'ordenes': [
            {'numero_orden': '001', 'dni': '12345678', 'estado': 'Finalizado'},
            {'numero_orden': '002', 'dni': '87654321', 'estado': 'En progreso'},
            {'numero_orden': '003', 'dni': '23456789', 'estado': 'Pendiente de entrega'},
            {'numero_orden': '004', 'dni': '98765432', 'estado': 'Finalizado'},
            {'numero_orden': '005', 'dni': '34567890', 'estado': 'En progreso'},
            {'numero_orden': '006', 'dni': '45678901', 'estado': 'Pendiente de entrega'},
            {'numero_orden': '007', 'dni': '56789012', 'estado': 'Finalizado'}
        ]
    }
    return render(request, 'web/administracion.html', contexto)