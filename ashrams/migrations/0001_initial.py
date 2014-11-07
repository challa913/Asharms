# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ashrams'
        db.create_table(u'ashrams_ashrams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 7, 0, 0))),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 7, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('age_groups', self.gf('django.db.models.fields.TextField')()),
            ('ashram_rating', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('ashrams', ['Ashrams'])


    def backwards(self, orm):
        # Deleting model 'Ashrams'
        db.delete_table(u'ashrams_ashrams')


    models = {
        'ashrams.ashrams': {
            'Meta': {'object_name': 'Ashrams'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'age_groups': ('django.db.models.fields.TextField', [], {}),
            'ashram_rating': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 7, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 7, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ashrams']