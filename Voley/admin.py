from django.contrib import admin

# Register your models here.

from .models import Equipo,Torneo, Fecha,Partido

admin.site.register(Torneo)
admin.site.register(Equipo)
admin.site.register(Fecha)
admin.site.register(Partido)
