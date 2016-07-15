from django.conf.urls import include, url
from . import views,TorneoViews,EquipoViews,FechaViews,PartidoViews
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.index,name='index'),
        url(r'^programacion', views.programacion,name='programacion'),
        url(r'^posiciones', views.posiciones2 ,name='posiciones'),
        url(r'^torneos', views.torneoLista),
        url(r'^posiciones/(?P<pk>[0-9]+)', views.posiciones, name='posiciones3'),
        url(r'^hola', views.hola),

        #URL Torneo
        url(r'^torneoas', TemplateView.as_view(template_name='Voley/torneo/index.html')),
        url(r'^torneo' , TorneoViews.torneoIndex, name='torneo_index'),

        url(r'^agregarTorneo/$', TorneoViews.torneo_nuevo, name='agregarTorneo'),
        url(r'^adminTorneo/(?P<pk>[0-9]+)', TorneoViews.torneoAdmin, name='adminTorneo'),
        url(r'^editarTorneo/(?P<pk>[0-9]+)', TorneoViews.editarTorneo, name='editarTorneo'),
        url(r'^eliminar/(?P<idTorneo>[0-9]+)/torneo', TorneoViews.eliminarTorneo, name='eliminarTorneo'),

        #URL Equipo
        url(r'^agregarEquipoTorneo/(?P<pk>[0-9]+)', EquipoViews.agregarEquipoTorneo, name='agregarEquipoTorneo'),
        url(r'^eliminarEquipoTorneo/(?P<idTorneo>[0-9]+)/(?P<idEquipo>[0-9]+)', EquipoViews.eliminarEquipoTorneo, name='eliminarEquipoTorneo'),

        url(r'^buscarEquipo/$', EquipoViews.buscarEquipo, name='selector_equipo'),
        url(r'^buscarEquipo1/$', EquipoViews.buscarEquipo1, name='selector_equipo1'),

        #URL Fechas
        url(r'^adminFecha/(?P<pk>[0-9]+)' , FechaViews.adminFechaTorneo, name='fecha_admin'),
        url(r'^agregarFecha/(?P<idTorneo>[0-9]+)', FechaViews.nuevaFecha, name='fecha_nueva'),
        url(r'^eliminarFecha/(?P<idFecha>[0-9]+)', FechaViews.eliminar_fecha, name='fecha_delete'),

        #URL Partido
        url(r'^nuevoPartido/(?P<idFecha>[0-9]+)', PartidoViews.nuevoPartido, name='nuevo_partido'),
        url(r'^actualizarPartido/(?P<idPartido>[0-9]+)', PartidoViews.actualizarPartido, name='actualizar_partido')
    ]
