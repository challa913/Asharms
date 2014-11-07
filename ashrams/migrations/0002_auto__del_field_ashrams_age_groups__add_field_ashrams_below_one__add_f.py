# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ashrams.age_groups'
        db.delete_column(u'ashrams_ashrams', 'age_groups')

        # Adding field 'Ashrams.below_one'
        db.add_column(u'ashrams_ashrams', 'below_one',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.one_to_five'
        db.add_column(u'ashrams_ashrams', 'one_to_five',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.six_to_ten'
        db.add_column(u'ashrams_ashrams', 'six_to_ten',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.eleven_to_fourteen'
        db.add_column(u'ashrams_ashrams', 'eleven_to_fourteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.fifteen_to_eighteen'
        db.add_column(u'ashrams_ashrams', 'fifteen_to_eighteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.nineteen_to_forty'
        db.add_column(u'ashrams_ashrams', 'nineteen_to_forty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.forty_to_sixty'
        db.add_column(u'ashrams_ashrams', 'forty_to_sixty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ashrams.above_sixty'
        db.add_column(u'ashrams_ashrams', 'above_sixty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Ashrams.age_groups'
        db.add_column(u'ashrams_ashrams', 'age_groups',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)

        # Deleting field 'Ashrams.below_one'
        db.delete_column(u'ashrams_ashrams', 'below_one')

        # Deleting field 'Ashrams.one_to_five'
        db.delete_column(u'ashrams_ashrams', 'one_to_five')

        # Deleting field 'Ashrams.six_to_ten'
        db.delete_column(u'ashrams_ashrams', 'six_to_ten')

        # Deleting field 'Ashrams.eleven_to_fourteen'
        db.delete_column(u'ashrams_ashrams', 'eleven_to_fourteen')

        # Deleting field 'Ashrams.fifteen_to_eighteen'
        db.delete_column(u'ashrams_ashrams', 'fifteen_to_eighteen')

        # Deleting field 'Ashrams.nineteen_to_forty'
        db.delete_column(u'ashrams_ashrams', 'nineteen_to_forty')

        # Deleting field 'Ashrams.forty_to_sixty'
        db.delete_column(u'ashrams_ashrams', 'forty_to_sixty')

        # Deleting field 'Ashrams.above_sixty'
        db.delete_column(u'ashrams_ashrams', 'above_sixty')


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
            'six_to_ten': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ashrams']