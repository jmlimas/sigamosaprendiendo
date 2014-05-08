# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table(u'inicio_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('grado', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('escuela', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tutor', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('Comentario', self.gf('django.db.models.fields.TextField')(max_length=700)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('hospital', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'inicio', ['Alumno'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table(u'inicio_alumno')


    models = {
        u'inicio.alumno': {
            'Comentario': ('django.db.models.fields.TextField', [], {'max_length': '700'}),
            'Meta': {'object_name': 'Alumno'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'escuela': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'grado': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'hospital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'tutor': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        }
    }

    complete_apps = ['inicio']