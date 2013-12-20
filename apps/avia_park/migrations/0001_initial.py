# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Craft'
        db.create_table(u'avia_park_craft', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'avia_park', ['Craft'])

        # Adding model 'CraftImage'
        db.create_table(u'avia_park_craftimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('craft', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['avia_park.Craft'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'avia_park', ['CraftImage'])


    def backwards(self, orm):
        # Deleting model 'Craft'
        db.delete_table(u'avia_park_craft')

        # Deleting model 'CraftImage'
        db.delete_table(u'avia_park_craftimage')


    models = {
        u'avia_park.craft': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'Craft'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'avia_park.craftimage': {
            'Meta': {'ordering': "['craft__title']", 'object_name': 'CraftImage'},
            'craft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['avia_park.Craft']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['avia_park']