# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageContent'
        db.create_table(u'core_pagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.CharField')(default='main_page', unique=True, max_length=50)),
            ('additional_header', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('additional_footer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slider_proxy', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'core', ['PageContent'])


    def backwards(self, orm):
        # Deleting model 'PageContent'
        db.delete_table(u'core_pagecontent')


    models = {
        u'core.pagecontent': {
            'Meta': {'ordering': "['page']", 'object_name': 'PageContent'},
            'additional_footer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'additional_header': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.CharField', [], {'default': "'main_page'", 'unique': 'True', 'max_length': '50'}),
            'slider_proxy': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']