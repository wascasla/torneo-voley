from django.shortcuts import render,render_to_response,redirect,get_object_or_404,RequestContext
from . models import *
from .forms import *

def adminFechaTorneo(request,pk):
    fecha = Fecha.objects.get(pk=pk)
    partidos = Partido.objects.filter(fecha=fecha)
    return  render(request,'Voley/fecha/adminFechaTorneo.html',{'fecha':fecha,'partidos':partidos})

def nuevaFecha(request,idTorneo):
    oTorneo = Torneo.objects.get(pk=idTorneo)
    if request.method == "POST":
        errores = []
        hayErrores = False
        nombreFecha = request.POST['nombreFecha']
        datosJornada = request.POST['datosJornada']

        if len(nombreFecha) == 0:
            errores.append("El campo Nombre no puede estar vacio")
            hayErrores = True

        if hayErrores:
            return render(request,'Voley/fecha/nuevaFecha.html',{'errores':errores,'nombreFecha':nombreFecha,'datosJornada':datosJornada,'oTorneo':oTorneo})
        else:
            nueva_fecha = Fecha(nombreFecha=nombreFecha,datosJornada=datosJornada,torneo=oTorneo)
            nueva_fecha.save()
            return redirect('adminTorneo', oTorneo.pk)
    else:
        return  render(request,'Voley/fecha/nuevaFecha.html',{'oTorneo':oTorneo})

def eliminar_fecha(request,idFecha):
    hayErrores =False
    errores = []
    b = Fecha.objects.get(pk=idFecha)
    idTorneo = b.torneo.pk
    #partidos = Partido.objects.get(fecha=b)
    if not Partido.objects.filter(fecha=b):
        b.delete()
        return redirect('adminTorneo', idTorneo)
    else:
        hayErrores=True
        errores.append("Esta fecha posee partido por lo cual no puede ser eliminada")
        partidos = Partido.objects.filter(fecha=b)
        return  render(request,'Voley/fecha/adminFechaTorneo.html',{'fecha':b,'hayErrores':hayErrores,'errores':errores,'partidos':partidos})
        #return redirect('fecha_admin', idFecha,hayErrores,errores)

