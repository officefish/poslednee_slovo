# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Hero.description'
        db.add_column(u'hero_hero', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Hero.description'
        db.delete_column(u'hero_hero', 'description')


    models = {
        u'hero.hero': {
            'Meta': {'object_name': 'Hero'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eptitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'vocation': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['hero']