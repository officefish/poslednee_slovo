# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hero'
        db.create_table(u'hero_hero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('vocation', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('eptitude', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'hero', ['Hero'])


    def backwards(self, orm):
        # Deleting model 'Hero'
        db.delete_table(u'hero_hero')


    models = {
        u'hero.hero': {
            'Meta': {'object_name': 'Hero'},
            'eptitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'vocation': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['hero']