# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RobotData'
        db.create_table(u'robots_robotdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal(u'robots', ['RobotData'])


    def backwards(self, orm):
        # Deleting model 'RobotData'
        db.delete_table(u'robots_robotdata')


    models = {
        u'robots.robotdata': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'RobotData'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['robots']