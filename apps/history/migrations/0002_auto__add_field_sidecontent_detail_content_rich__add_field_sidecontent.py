# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SideContent.detail_content_rich'
        db.add_column(u'history_sidecontent', 'detail_content_rich',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SideContent.detail_content_plane'
        db.add_column(u'history_sidecontent', 'detail_content_plane',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SideContent.detail_img_adjustment'
        db.add_column(u'history_sidecontent', 'detail_img_adjustment',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SideContent.detail_content_rich'
        db.delete_column(u'history_sidecontent', 'detail_content_rich')

        # Deleting field 'SideContent.detail_content_plane'
        db.delete_column(u'history_sidecontent', 'detail_content_plane')

        # Deleting field 'SideContent.detail_img_adjustment'
        db.delete_column(u'history_sidecontent', 'detail_img_adjustment')


    models = {
        u'history.contentblock': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'ContentBlock'},
            'content_plane': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_rich': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'history.sidecontent': {
            'Meta': {'ordering': "['content_block', 'side', '-weight', '-pub_date_start']", 'object_name': 'SideContent'},
            'content_block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['history.ContentBlock']"}),
            'content_plane': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_rich': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'detail_content_plane': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'detail_content_rich': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'detail_img_adjustment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['history']