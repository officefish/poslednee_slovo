# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hero'
        db.create_table(u'card_hero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'card', ['Hero'])

        # Adding model 'Book'
        db.create_table(u'card_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'card', ['Book'])

        # Adding M2M table for field heroes on 'Book'
        m2m_table_name = db.shorten_name(u'card_book_heroes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'card.book'], null=False)),
            ('hero', models.ForeignKey(orm[u'card.hero'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'hero_id'])

        # Adding field 'Card.book'
        db.add_column(u'card_card', 'book',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['card.Book'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Hero'
        db.delete_table(u'card_hero')

        # Deleting model 'Book'
        db.delete_table(u'card_book')

        # Removing M2M table for field heroes on 'Book'
        db.delete_table(db.shorten_name(u'card_book_heroes'))

        # Deleting field 'Card.book'
        db.delete_column(u'card_card', 'book_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'card.book': {
            'Meta': {'object_name': 'Book'},
            'heroes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['card.Hero']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'card.card': {
            'Meta': {'object_name': 'Card'},
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Book']", 'null': 'True', 'blank': 'True'}),
            'card_type': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Race']", 'null': 'True', 'blank': 'True'}),
            'subrace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.SubRace']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'unit_type': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'card.cardeptitude': {
            'Meta': {'object_name': 'CardEptitude'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Card']"}),
            'dependency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.CardEptitude']", 'null': 'True', 'blank': 'True'}),
            'eptitude_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'period': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Race']", 'null': 'True', 'blank': 'True'}),
            'subrace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.SubRace']", 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'unit'", 'null': 'True', 'to': u"orm['card.Card']"})
        },
        u'card.collection': {
            'Meta': {'object_name': 'Collection'},
            'cards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['card.Card']", 'through': u"orm['card.Collector']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {'default': '35'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'collection_owner'", 'to': u"orm['auth.User']"})
        },
        u'card.collector': {
            'Meta': {'object_name': 'Collector'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'collection_card'", 'to': u"orm['card.Card']"}),
            'collection_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'card.hero': {
            'Meta': {'object_name': 'Hero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'card.race': {
            'Meta': {'object_name': 'Race'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'card.subrace': {
            'Meta': {'object_name': 'SubRace'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['card.Race']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['card']