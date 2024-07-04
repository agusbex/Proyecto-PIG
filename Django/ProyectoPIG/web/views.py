from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import ContactoForm, SeguimientoForm 
from .models import Orden 
import datetime
from .forms import OrdenForm
from django.shortcuts import get_object_or_404

def index(request):
    context = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now()
    }
    return render(request, 'web/index.html', context)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tu consulta ha sido enviada con éxito')
            return redirect('index')
        else:
            data["form"] = formulario
    return render(request, "web/contacto.html", data)

def user_logout(request):
    logout(request)
    messages.success(request, 'Sessión cerrada con éxito')
    return redirect('index')


def saludar(request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre}</h1>")


def seguimiento(request):
    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            numero_orden = form.cleaned_data['numero_orden']
            dni = form.cleaned_data['dni']
            orden = Orden.objects.filter(numero_orden=numero_orden, dni=dni).first()
            if orden:
                return render(request, 'web/detalle_orden.html', {'orden': orden})
            else:
                messages.error(request, 'No se encontró la orden.')
    else:
        form = SeguimientoForm()
    return render(request, 'web/seguimiento.html', {'form': form})


def administracion(request):
    ordenes = Orden.objects.all()
    return render(request, 'web/administracion.html', {'ordenes': ordenes})

def editar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('administracion')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'web/editar_orden.html', {'form': form})

def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('administracion')
    return render(request, 'web/confirmar_eliminacion.html', {'orden': orden})

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administracion')
    else:
        form = OrdenForm()
    return render(request, 'web/crear_orden.html', {'form': form})
