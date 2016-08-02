from django.contrib import admin

# Register your models here.

from .models import Equipo,Torneo, Fecha,Partido,Persona,Jugador,Arbitro

admin.site.register(Torneo)
admin.site.register(Equipo)
admin.site.register(Fecha)
admin.site.register(Partido)
admin.site.register(Persona)
admin.site.register(Jugador)
admin.site.register(Arbitro)
