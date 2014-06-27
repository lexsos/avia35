# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agent'
        db.create_table(u'schedule_agent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Agent'])

        # Adding model 'Flight'
        db.create_table(u'schedule_flight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('departure', self.gf('django.db.models.fields.TextField')()),
            ('arrival', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Flight'])

        # Adding M2M table for field agents on 'Flight'
        m2m_table_name = db.shorten_name(u'schedule_flight_agents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flight', models.ForeignKey(orm[u'schedule.flight'], null=False)),
            ('agent', models.ForeignKey(orm[u'schedule.agent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['flight_id', 'agent_id'])

        # Adding model 'Note'
        db.create_table(u'schedule_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'schedule', ['Note'])

        # Adding model 'PaymentBanner'
        db.create_table(u'schedule_paymentbanner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('pub_date_start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('pub_date_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'schedule', ['PaymentBanner'])


    def backwards(self, orm):
        # Deleting model 'Agent'
        db.delete_table(u'schedule_agent')

        # Deleting model 'Flight'
        db.delete_table(u'schedule_flight')

        # Removing M2M table for field agents on 'Flight'
        db.delete_table(db.shorten_name(u'schedule_flight_agents'))

        # Deleting model 'Note'
        db.delete_table(u'schedule_note')

        # Deleting model 'PaymentBanner'
        db.delete_table(u'schedule_paymentbanner')


    models = {
        u'schedule.agent': {
            'Meta': {'ordering': "['title']", 'object_name': 'Agent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'schedule.flight': {
            'Meta': {'ordering': "['-weight', 'direction']", 'object_name': 'Flight'},
            'agents': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schedule.Agent']", 'symmetrical': 'False', 'blank': 'True'}),
            'arrival': ('django.db.models.fields.TextField', [], {}),
            'departure': ('django.db.models.fields.TextField', [], {}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'schedule.note': {
            'Meta': {'ordering': "['-weight', 'content']", 'object_name': 'Note'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'schedule.paymentbanner': {
            'Meta': {'ordering': "['-weight', 'title']", 'object_name': 'PaymentBanner'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['schedule']