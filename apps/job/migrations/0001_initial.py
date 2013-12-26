# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vacancy'
        db.create_table(u'job_vacancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('requirements', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('schedule', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('payment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'job', ['Vacancy'])

        # Adding model 'VacancyResponse'
        db.create_table(u'job_vacancyresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vacancy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['job.Vacancy'])),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('about_self', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('summary', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'job', ['VacancyResponse'])


    def backwards(self, orm):
        # Deleting model 'Vacancy'
        db.delete_table(u'job_vacancy')

        # Deleting model 'VacancyResponse'
        db.delete_table(u'job_vacancyresponse')


    models = {
        u'job.vacancy': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'Vacancy'},
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