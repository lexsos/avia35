# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'feedback_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'feedback_question')


    models = {
        u'feedback.question': {
            'Meta': {'ordering': "['-create_date']", 'object_name': 'Question'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']