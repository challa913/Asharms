# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ashrams.phone'
        db.add_column(u'ashrams_ashrams', 'phone',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ashrams.phone'
        db.delete_column(u'ashrams_ashrams', 'phone')


    models = {
        'ashrams.ashrams': {
            'Meta': {'object_name': 'Ashrams'},
            'above_sixty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'ashram_rating': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'below_one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 7, 0, 0)'}),
            'eleven_to_fourteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fifteen_to_eighteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'forty_to_sixty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 7, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nineteen_to_forty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one_to_five': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'six_to_ten': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ashrams']