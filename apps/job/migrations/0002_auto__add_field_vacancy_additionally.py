# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vacancy.additionally'
        db.add_column(u'job_vacancy', 'additionally',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vacancy.additionally'
        db.delete_column(u'job_vacancy', 'additionally')


    models = {
        u'job.vacancy': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'Vacancy'},
            'additionally': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'job.vacancyresponse': {
            'Meta': {'ordering': "['-create_date']", 'object_name': 'VacancyResponse'},
            'about_self': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'summary': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'vacancy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['job.Vacancy']"})
        }
    }

    complete_apps = ['job']