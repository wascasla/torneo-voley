# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-25 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreIdentificativo', models.CharField(max_length=10, null=True)),
                ('nombreEquipo', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreFecha', models.CharField(max_length=10)),
                ('datosJornada', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPartido', models.DateField(blank=True, null=True)),
                ('horaPartido', models.TimeField(blank=True, null=True)),
                ('datosPartido', models.CharField(blank=True, max_length=40, null=True)),
                ('golLocal', models.IntegerField(blank=True, null=True)),
                ('golVisitante', models.IntegerField(blank=True, null=True)),
                ('cargado', models.BooleanField(default=False)),
                ('fecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voley.Fecha')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partido_local_equipo', to='Voley.Equipo')),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partido_visitante_equipo', to='Voley.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTorneo', models.IntegerField()),
                ('pj', models.IntegerField(blank=True)),
                ('pg', models.IntegerField(blank=True)),
                ('pp', models.IntegerField(blank=True)),
                ('pe', models.IntegerField(blank=True)),
                ('gf', models.IntegerField(blank=True)),
                ('gc', models.IntegerField(blank=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voley.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('localidad', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=30, null=True)),
                ('fechaRegistro', models.DateField(default=django.utils.timezone.now)),
                ('fechaInicio', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=False)),
                ('equipos', models.ManyToManyField(to='Voley.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='fecha',
            name='torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voley.Torneo'),
        ),
    ]