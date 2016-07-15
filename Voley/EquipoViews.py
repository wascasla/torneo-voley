from django.shortcuts import render,render_to_response,redirect,get_object_or_404,RequestContext
from . models import *
from .forms import *

def agregarEquipoTorneo(request,pk):
    if request.method == "POST":
        hayErrores = False
        errores = []
        equipoId = request.POST['hequipo']
        mensaje = []
        yaExiste = False
        if len(equipoId) == 0:
            hayErrores = True
            errores.append("Debe Seleccionar un Equipo para agregar al Torneo")
            return  render(request,'Voley/equipo/agregarEquipoTorneo.html',{'errores':errores,'torneoId':pk})
        else:
            torneo = Torneo.objects.get(pk=pk)
            equipo = Equipo.objects.get(pk=equipoId)

            #pregunto si el equipo ya esta agregado al torneo, si no lo agrego, si ya esta mando error
            for e in torneo.equipos.all():
                if e == equipo:
                    yaExiste = True
                    errores.append("El equipo que quiere agregar ya esta en el Torneo!!!")
                    return  render(request,'Voley/equipo/agregarEquipoTorneo.html',{'errores':errores,'torneoId':pk,'torneo':torneo})

            torneo.equipos.add(equipo)
            mensaje.append("Equipo cargado con exito")
            return  render(request,'Voley/equipo/agregarEquipoTorneo.html',{'torneoId':pk,'torneo':torneo,'mensaje':mensaje})


    else:
        torneo = Torneo.objects.get(pk=pk)
        return  render(request,'Voley/equipo/agregarEquipoTorneo.html',{'torneoId':pk,'torneo':torneo})

#selector equipo
def buscarEquipo(request):
    if request.method == "POST":
        q = request.POST['nombre']
        hayErrores = False
        errores = []
        equipos = []
        if q:
            equipos = Equipo.objects.filter(nombreEquipo__icontains=q)
        else:
            hayErrores = True
            errores.append("No exiten equipos con ese nombre")


        form = buscadorEquipoForm()
        if len(equipos) != 0:
            return render(request, 'Voley/selectores/selectorEquipo.html', {'equipos':equipos, 'form':form})
        else:
            return render(request, 'Voley/selectores/selectorEquipo.html', {'form':form, 'errores':errores})
    else:
        form = buscadorEquipoForm()
        equipos = Equipo.objects.all()
        return render(request, 'Voley/selectores/selectorEquipo.html', {'equipos':equipos, 'form':form})

#selector equipo1
def buscarEquipo1(request):
    if request.method == "POST":
        q = request.POST['nombre']
        hayErrores = False
        errores = []
        equipos = []
        if q:
            equipos = Equipo.objects.filter(nombreEquipo__icontains=q)
        else:
            hayErrores = True
            errores.append("No exiten equipos con ese nombre")


        form = buscadorEquipoForm()
        if len(equipos) != 0:
            return render(request, 'Voley/selectores/selectorEquipo1.html', {'equipos':equipos, 'form':form})
        else:
            return render(request, 'Voley/selectores/selectorEquipo1.html', {'form':form, 'errores':errores})
    else:
        form = buscadorEquipoForm()
        equipos = Equipo.objects.all()
        return render(request, 'Voley/selectores/selectorEquipo1.html', {'equipos':equipos, 'form':form})

def eliminarEquipoTorneo(request,idTorneo,idEquipo):
    mensaje = []
    torneo = Torneo.objects.get(pk=idTorneo)
    equipo = Equipo.objects.get(pk=idEquipo)
    torneo.equipos.remove(equipo)
    mensaje.append("Equipo eliminado con exito")
    return  render(request,'Voley/equipo/agregarEquipoTorneo.html',{'torneoId':idTorneo,'torneo':torneo,'mensaje':mensaje})