# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DocumentCounter'
        db.create_table(u'documents_documentcounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Document'])),
            ('client_ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'documents', ['DocumentCounter'])


    def backwards(self, orm):
        # Deleting model 'DocumentCounter'
        db.delete_table(u'documents_documentcounter')


    models = {
        u'documents.document': {
            'Meta': {'ordering': "['-weight', 'pub_date_start']", 'object_name': 'Document'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.DocumentCategory']"}),
            'doc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.DocumentType']"}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'documents.documentcategory': {
            'Meta': {'ordering': "['-weight', 'pub_date_start']", 'object_name': 'DocumentCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'documents.documentcounter': {
            'Meta': {'ordering': "['access_date']", 'object_name': 'DocumentCounter'},
            'access_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'client_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'documents.documenttype': {
            'Meta': {'ordering': "['title']", 'object_name': 'DocumentType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['documents']