# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Document.category'
        category_pk = 1
        try:
            from documents.models import DocumentCategory
            category_pk = DocumentCategory.objects.all()[0].pk
        except:
            pass

        db.alter_column(u'documents_document', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=category_pk, to=orm['documents.DocumentCategory']))

    def backwards(self, orm):

        # Changing field 'Document.category'
        db.alter_column(u'documents_document', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.DocumentCategory'], null=True))

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
            'Meta': {'ordering': "['title']", 'object_name': 'DocumentCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'documents.documenttype': {
            'Meta': {'ordering': "['title']", 'object_name': 'DocumentType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['documents']
