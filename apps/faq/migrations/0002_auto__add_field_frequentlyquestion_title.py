# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FrequentlyQuestion.title'
        db.add_column(u'faq_frequentlyquestion', 'title',
                      self.gf('django.db.models.fields.CharField')(default='title', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FrequentlyQuestion.title'
        db.delete_column(u'faq_frequentlyquestion', 'title')


    models = {
        u'faq.frequentlyquestion': {
            'Meta': {'ordering': "['-weight', '-pub_date_start']", 'object_name': 'FrequentlyQuestion'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date_start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['faq']