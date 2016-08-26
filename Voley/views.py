from django.shortcuts import render,RequestContext
from . models import *
from django.db import connection
#import psycopg2, psycopg2.extras

# Create your views here.
from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView

def index(request):
	return render(request,'Voley/index.html', {})

def programacion(request):
    fechas = Fecha.objects.all()
    return render(request,'Voley/programacion.html', {})

def posiciones2(request):
    pos = Posicion.objects.all().order_by('-puntos')
    return render(request,'Voley/posiciones.html', {'posiciones':pos})

def torneoLista(request):
    torneos = Torneo.objects.all()
    return render(request,'Voley/torneo/torneosLista.html', {'torneos':torneos})

def posiciones(request,pk):
    cursor = connection.cursor()
    #ret = cursor.callproc("pos2", (pk))# calls PROCEDURE named LOG_MESSAGE which resides in MY_UTIL Package
    ret = cursor.execute("SELECT * from pos2(1) as (a varchar(20),pj bigint ,pg bigint , pp bigint , pe bigint , gf bigint )")
    #ret = [row[0] for row in cursor.fetchall()]
    #ret = cursor.fetchall()
    ret = [row[0] for row in cursor.fetchall()]
    cursor.close()
    #return ret
    #torneos = Torneo.objects.all()
    return render(request,'Voley/torneo/posiciones.html', {'tabla':ret})
    #return render(request,'Voley/torneo/posiciones.html', {})

def hola(request):
    #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor
    cursor = connection.cursor()
    #cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #ret = cursor.callproc("pos2", (pk))# calls PROCEDURE named LOG_MESSAGE which resides in MY_UTIL Package
    cursor.execute("SELECT * from pos2(1) as (a varchar(20),pj bigint ,pg bigint , pp bigint , pe bigint , gf bigint )")
    #nombres = [row[0] for row in cursor.fetchall()]
    #pg = [row[1] for row in cursor.fetchall()]
    ret = cursor.fetchall()
    cursor.close()
    #torneos = Torneo.objects.all()
    #return render_to_response(request,'Voley/torneo/hola.html', {'tabla':ret}, context_instance=RequestContext(request))
    return render_to_response('Voley/torneo/hola.html', {'tabla':ret}, context_instance=RequestContext(request))