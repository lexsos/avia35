# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContentBlock'
        db.create_table(u'history_contentblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_rich', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_plane', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'history', ['ContentBlock'])

        # Adding model 'SideContent'
        db.create_table(u'history_sidecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['history.ContentBlock'])),
            ('content_rich', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_plane', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'history', ['SideContent'])


    def backwards(self, orm):
        # Deleting model 'ContentBlock'
        db.delete_table(u'history_contentblock')

        # Deleting model 'SideContent'
        db.delete_table(u'history_sidecontent')


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
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'SideContent'},
            'content_block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['history.ContentBlock']"}),
            'content_plane': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_rich': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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