# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_alarm_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmComunidad',
            fields=[
                ('alarm_comunidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('alarm_descripcion', models.IntegerField(blank=True, null=True)),
                ('alarm_total_personas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmCordanadas',
            fields=[
                ('alarm_id_coordena', models.AutoField(primary_key=True, serialize=False)),
                ('alarm_number', models.CharField(blank=True, max_length=255, null=True)),
                ('alarm_comunidadalarm_comunidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_alarm_api.AlarmComunidad')),
            ],
        ),
        migrations.CreateModel(
            name='AlarmDatosEmergencia',
            fields=[
                ('alarm_id_datos', models.AutoField(primary_key=True, serialize=False)),
                ('alarm_numero_emerge', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmRol',
            fields=[
                ('alarm_idrol', models.AutoField(primary_key=True, serialize=False)),
                ('alarm_descripcion', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlarmUserComunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_comunidadalarm_comunidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_alarm_api.AlarmComunidad')),
                ('alarm_rolalarm_idrol', models.ForeignKey(db_column='alarm_rolalarm_idrol', on_delete=django.db.models.deletion.DO_NOTHING, to='app_alarm_api.AlarmRol')),
            ],
        ),
        migrations.CreateModel(
            name='AlarmUsuarios',
            fields=[
                ('alarm_id_user', models.AutoField(primary_key=True, serialize=False)),
                ('alarm_correo', models.CharField(max_length=255)),
                ('alarm_nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('alarm_apelldio', models.CharField(blank=True, max_length=255, null=True)),
                ('alarm_usuario', models.CharField(blank=True, max_length=255, null=True)),
                ('alar_edad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='alarmusercomunidad',
            name='alarm_usuariosalarm_id_user',
            field=models.ForeignKey(db_column='alarm_usuariosalarm_id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='app_alarm_api.AlarmUsuarios'),
        ),
    ]
