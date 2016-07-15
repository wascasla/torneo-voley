from django.shortcuts import render,render_to_response,redirect,get_object_or_404,RequestContext
from . models import *
from django.db import connection
import psycopg2, psycopg2.extras

# Create your views here.
#from django.shortcuts import render,render_to_response
#from django.views.generic.base import TemplateView
#
#from django.core.urlresolvers import reverse_lazy
#from django.views.generic import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import (
#    CreateView,
#    UpdateView,
#    DeleteView
#)
#from .models import Torneo

def torneoIndex(request):
    torneos = Torneo.objects.all()
    return render(request,'Voley/torneo/index.html', {'torneos':torneos})

#class TorneoList(ListView):
#    model = Torneo
#class TorneoDetail(DetailView):
#    model = Torneo
#class TorneoCreation(CreateView):
#    model = Torneo
#    success_url = reverse_lazy('torneos:list')
#    fields = ['nombre', 'telefono', 'localidad', 'direccion','fechaInicio']
#class TorneoUpdate(UpdateView):
#    model = Torneo
#    success_url = reverse_lazy('torneos:list')
#    fields = ['nombre', 'telefono', 'localidad', 'direccion','fechaInicio']
#class TorneoDelete(DeleteView):
#    model = Torneo
#    success_url = reverse_lazy('torneos:list')

#desde aqui los metodos abm
#def torneo_nuevo(request):
#	if request.method == "POST":
#        errores = []
#		hayErrores = False
#		nombre = request.POST['nombre']
#            #telefono = request.POST['telefono']
#            #direccion = request.POST['direccion']
#            #localidad = request.POST['localidad']
#            #fechaInicio = request.POST['fechaInicio']
#
#
#        if 	hayErrores:
#            return render(request, 'Voley/torneo/nuevoTorneo.html', {'errores':errores,'fechaInicio':fechaInicio})
#        else:
#            nuevoTorneo = Torneo(fecha_inicio=fechaInicio,nombre = nombre, telefono = telefono,direccion = direccion,localidad=localidad)
#            nuevoTorneo.save()
#            return redirect('torneo_index')
#
#	else:
#		return render(request, 'agregarTorneo', {})

def torneo_nuevo(request):
    if request.method == "POST":
        errores = []
        hayErrores = False
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        fechaInicio = request.POST['fechaInicio']
        direccion = request.POST['direccion']
        localidad = request.POST['localidad']

        if len(fechaInicio) == 0:
            fechaInicio = None

        if len(nombre) == 0:
            errores.append("El campo Nombre no puede estar vacio")
            hayErrores = True

        if hayErrores:
            return render(request,'Voley/torneo/nuevoTorneo.html',{'errores':errores,'fechaInicio':fechaInicio,'nombre':nombre,'telefono':telefono,
            'direccion':direccion,'localidad':localidad})
        else:
            nuevoTorneo = Torneo(fechaInicio=fechaInicio,nombre=nombre,localidad=localidad,direccion=direccion,telefono=telefono)
            nuevoTorneo.save()
            return redirect('torneo_index')
    else:
        return  render(request,'Voley/torneo/nuevoTorneo.html',{})

def torneoAdmin(request,pk):
    torneo = get_object_or_404(Torneo,pk=pk)
    if torneo:
        fechas = Fecha.objects.filter(torneo=torneo.pk)
        posiciones = Posicion.objects.filter(idTorneo=torneo.pk).order_by('-puntos')
    return  render(request,'Voley/torneo/adminTorneo.html',{'torneo':torneo,'fechas':fechas,'posiciones':posiciones})

def editarTorneo(request,pk):
    torneo = Torneo.objects.get(pk=pk)
    #return render(request,'Voley/torneo/editar.html',{'torneo':torneo,'fechaInicio':torneo.fechaInicio,'nombre':torneo.nombre,'telefono':torneo.telefono,'direccion':torneo.direccion,'localidad':torneo.direccion})
    if request.method == "POST":
        errores = []
        hayErrores = False
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        fechaInicio = request.POST['fechaInicio']
        direccion = request.POST['direccion']
        localidad = request.POST['localidad']

        if len(fechaInicio) == 0:
            fechaInicio = None

        if len(nombre) == 0:
            errores.append("El campo Nombre no puede estar vacio")
            hayErrores = True

        if hayErrores:
            return render(request,'Voley/torneo/editar.html',{'errores':errores,'fechaInicio':fechaInicio,'nombre':nombre,'telefono':telefono,
            'direccion':direccion,'localidad':localidad})
        else:
            torneo.fechaInicio=fechaInicio
            torneo.nombre=nombre
            torneo.localidad=localidad
            torneo.direccion=direccion
            torneo.telefono=telefono
            torneo.save()
            #tiene que retornar al torneo admin
            return redirect('torneo_index')
    else:
        return render(request,'Voley/torneo/editar.html',{'torneo':torneo,'fechaInicio':torneo.fechaInicio,'nombre':torneo.nombre,'telefono':torneo.telefono,
            'direccion':torneo.direccion,'localidad':torneo.direccion})

def eliminarTorneo(request,idTorneo):
    errores = []
    hayErrores = False
    torneo = Torneo.objects.get(pk=idTorneo)
    fechas = Fecha.objects.filter(torneo=torneo)
    if fechas:
        hayErrores = True
        errores.append("Este torneo no puede ser eliminado ya que posee equipos o fechas creadas")
        return render(request,'Voley/torneo/editar.html',{'torneo':torneo,'errores':errores,'fechaInicio':torneo.fechaInicio,'nombre':torneo.nombre,'telefono':torneo.telefono,
            'direccion':torneo.direccion,'localidad':torneo.direccion})
    else:
        torneo.delete()
        return redirect('torneo_index')

