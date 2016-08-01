from django.shortcuts import render,render_to_response,redirect,get_object_or_404,RequestContext
from . models import *
from .forms import *

def nuevoPartido(request,idFecha):
    fecha = Fecha.objects.get(pk=idFecha)
    if request.method == "POST":
        errores = []
        hayErrores = False
        idequipoLocal = request.POST['hequipo']
        idequipoVisitante = request.POST['hequipo1']
        fechaPartido = request.POST['fechaPartido']
        hora = request.POST['horaPartido']
        datosPartido = request.POST['datosPartido']


        if len(fechaPartido) == 0:
            fechaPartido = None

        if len(hora) == 0:
            hora = None

        #en esta parte se chequea si el usuario eligio un equipo, y luego lo busca al objeto en la base de datos y lo asigna
        if len(idequipoLocal) == 0:
            errores.append("Debe seleccionar un Equipo Local ")
            hayErrores = True
        else:
            #chequer = chequearYaExistePartidoConEquipoEnLaFecha(idFecha,idequipoLocal)
            #if chequer:
            #    errores.append("Ya existe un Partido con el Equipo Local Elegido en esta fecha ")
            #    hayErrores = True
            equipoLocal = Equipo.objects.get(pk=idequipoLocal)

        #en esta parte se chequea si el usuario eligio un equipo, y luego lo busca al objeto en la base de datos y lo asigna
        if len(idequipoVisitante) == 0:
            errores.append("Debe seleccionar un Equipo Visitante ")
            hayErrores = True
        else:
            #chequer = chequearYaExistePartidoConEquipoEnLaFecha(idFecha,idequipoVisitante)
            #if chequer:
            #    errores.append("Ya existe un Partido con el Equipo Visitante Elegido en esta fecha")
            #    hayErrores = True
            equipoVisitante = Equipo.objects.get(pk=idequipoVisitante)

        if len(idequipoVisitante) != 0 and len(idequipoLocal) != 0:
            resultado = controlarMismoPartidoMismaFecha(idFecha,idequipoLocal,idequipoVisitante)
            #resultado = True

            if resultado:
                hayErrores = True
                errores.append("ya existe un partido con estos equipos en esta fecha")


        if hayErrores:
            return render(request,'Voley/partido/nuevo.html',{'fecha':fecha,'errores':errores,'fechaPartido':fechaPartido,'hora':hora,'datosPartido':datosPartido,
            'equipoLocal':equipoLocal,'equipoVisitante':equipoVisitante})
        else:
            nuevoPartido = Partido(fechaPartido=fechaPartido,horaPartido=hora,datosPartido=datosPartido,fecha=fecha,local=equipoLocal,visitante=equipoVisitante)
            nuevoPartido.save()
            #actualizarPosiciones(idFecha,equipoLocal.pk)
            #actualizarPosiciones(idFecha,equipoVisitante.pk)
            return redirect('fecha_admin',pk = idFecha )
    else:
        return  render(request,'Voley/partido/nuevo.html',{'fecha':fecha})


#actualizar datos del partido
def actualizarPartido(request,idPartido):
    partido = Partido.objects.get(pk=idPartido)
    equipoLocal = Equipo.objects.get(pk=partido.local.pk)
    equipoVisitante = Equipo.objects.get(pk=partido.visitante.pk)
    if request.method == "POST":
        errores = []
        hayErrores = False
        #equipoLocal = request.POST['hequipo']
        #equipoVisitante = request.POST['hequipo1']
        fechaPartido = request.POST['fechaPartido']
        hora = request.POST['horaPartido']
        datosPartido = request.POST['datosPartido']
        setLocal = request.POST['golesLocal']
        setVisitante = request.POST['golesVisitante']

        if len(fechaPartido) == 0:
            fechaPartido = None

        if len(hora) == 0:
            hora = None

        if len(setLocal) != 0:
            if len(setLocal) not in [0,1,2]:
                hayErrores = True
                errores.append("El valor del set Local debe estar dentro de los siguientes valores [0,1,2] "+setLocal)
        else:
            setLocal = None

        if len(setVisitante) != 0:
            if int(setVisitante) not in [0,1,2]:
                hayErrores = True
                errores.append("El valor del set Visitante debe estar dentro de los siguientes valores [0,1,2]"+setVisitante)
        else:
            setVisitante = None

        if hayErrores:
            return render(request,'Voley/partido/actualizar.html',{'partido':partido,'errores':errores,'fechaPartido':fechaPartido,'hora':hora,'datosPartido':datosPartido,
            'equipoLocal':equipoLocal,'equipoVisitante':equipoVisitante,'golesLocal':setLocal,'golesVisitante':setVisitante})
        else:
            partido.datosPartido = datosPartido
            partido.fechaPartido = fechaPartido
            partido.horaPartido = hora
            partido.golVisitante = setVisitante
            partido.golLocal = setLocal
            partido.save()

            if len(setLocal) != 0 and len(setVisitante) != 0:
                actualizarPosiciones(partido.fecha.pk,equipoLocal.pk)
                actualizarPosiciones(partido.fecha.pk,equipoVisitante.pk)
            return redirect('fecha_admin',pk = partido.fecha.pk )

    else:
        return render(request,'Voley/partido/actualizar.html',{'partido':partido,'fechaPartido':partido.fechaPartido,'hora':partido.horaPartido,'datosPartido':partido.datosPartido,
            'equipoLocal':equipoLocal,'equipoVisitante':equipoVisitante,'golesLocal':partido.golLocal,'golesVisitante':partido.golVisitante})



def controlarMismoPartidoMismaFecha(idFecha,eLocal,eVisitante):
    fecha = Fecha.objects.get(pk=idFecha)
    error = False
    #partido1 = Partido.objects.filter(fecha=fecha, local = eLocal, visitante = eVisitante)
    #partido2 = Partido.objects.filter(fecha=fecha, local = eVisitante, visitante = eLocal )

    #if partido1  | partido2:
    #    error = True

    if Partido.objects.filter(fecha=fecha, local = eLocal, visitante = eVisitante).exists() | \
            Partido.objects.filter(fecha=fecha, local = eVisitante, visitante = eLocal ).exists():
        error = True
    return error

def chequearYaExistePartidoConEquipoEnLaFecha(idFecha,equipo):
    fecha = Fecha.objects.get(pk=idFecha)
    error = False
    if Partido.objects.filter(fecha=fecha, local = equipo).exists() | \
            Partido.objects.filter(fecha=fecha, visitante = equipo ).exists():
        error = True
    return error


def actualizarPosiciones(idFecha,eLocal):
    pj = 0
    pg = 0
    ppa1 = 0 #pp partido perdidos a 1
    ppa0 = 0  #pe partido perdido a 0
    setFavor = 0
    setContra = 0
    valor = False
    fecha = Fecha.objects.get(pk=idFecha)
    torneo = Torneo.objects.get(pk=fecha.torneo.pk)
    fechasDelTorneo = Fecha.objects.filter(torneo=torneo)
    equipo = Equipo.objects.get(pk=eLocal)
    for f in fechasDelTorneo:
        #obtengo todos los ppartidos de cada fecha en donde aparezca el equipo
        partidos1 = Partido.objects.filter(fecha=f,local=eLocal)
        partidos2 = Partido.objects.filter(fecha=f,visitante=eLocal)
        if partidos1:
            #recorro los partidos en los que esta el equipo para tomar los datos
            for p in partidos1:
                if p.golVisitante!=None and p.golLocal!=None:
                    valor = True
                    pj = pj + 1
                    setFavor = setFavor + p.golLocal
                    setContra = setContra + p.golVisitante
                    if p.golLocal == 2 and p.golVisitante == 0:
                        pg = pg+1
                    #pregunto si gano 2 a 1
                    if p.golLocal == 2 and p.golVisitante == 1:
                        pg = pg+1
                    #pregunto si es partido perdido a 0
                    if p.golLocal == 0 and p.golVisitante == 2:
                        ppa0 = ppa0+1
                    #pregunto si es partido perdido a 1
                    if p.golLocal == 1 and p.golVisitante == 2:
                        ppa1 = ppa1+1


        if partidos2:
            #recorro los partidos en los que esta el equipo para tomar los datos
            for p in partidos2:
                if p.golVisitante!=None and p.golLocal!=None:
                    valor = True
                    pj = pj + 1
                    setFavor = setFavor + p.golVisitante
                    setContra = setContra + p.golLocal
                    if p.golVisitante == 2 and p.golLocal == 0:
                        pg = pg+1
                    #pregunto si gano 2 a 1
                    if p.golVisitante == 2 and p.golLocal == 1:
                        pg = pg+1
                    #pregunto si es partido perdido a 0
                    if p.golVisitante == 0 and p.golLocal == 2:
                        ppa0 = ppa0+1
                    #pregunto si es partido perdido a 1
                    if p.golVisitante == 1 and p.golLocal == 2:
                        ppa1 = ppa1+1

    #pregunto si tiene algo para guardar los datos o para update
    #if partidos1 or partidos2:
    if valor:
        if Posicion.objects.filter(idTorneo = torneo.pk, equipo = equipo).exists():
            pos = Posicion.objects.get(idTorneo = torneo.pk, equipo = equipo)
            pos.pj = pj
            pos.pg=pg
            pos.ppa1=ppa1
            pos.ppa0=ppa0
            pos.gf=setFavor
            pos.gc=setContra
            pos.coefSet = 0
            pos.puntos = pg*3+ppa0*1+ppa1*1
            pos.save()
        else:
            nuevoPos = Posicion(idTorneo = torneo.pk, equipo = equipo,pj=pj,pg=pg,ppa1=ppa1,ppa0=ppa0,gf=setFavor,gc=setContra,coefSet= 0,puntos = pg*3+ppa0*1+ppa1*1)
            nuevoPos.save()