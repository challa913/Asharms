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
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 8, 0, 0))),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 8, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('below_one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('one_to_five', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('six_to_ten', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('eleven_to_fourteen', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fifteen_to_eighteen', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nineteen_to_forty', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('forty_to_sixty', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('above_sixty', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ashram_rating', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('ashrams', ['Ashrams'])


    def backwards(self, orm):
        # Deleting model 'Ashrams'
        db.delete_table(u'ashrams_ashrams')


    models = {
        'ashrams.ashrams': {
            'Meta': {'object_name': 'Ashrams'},
            'above_sixty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'ashram_rating': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'below_one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 8, 0, 0)'}),
            'eleven_to_fourteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fifteen_to_eighteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'forty_to_sixty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 8, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nineteen_to_forty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one_to_five': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'six_to_ten': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ashrams']