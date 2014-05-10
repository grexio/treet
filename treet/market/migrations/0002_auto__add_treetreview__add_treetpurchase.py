# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TreetReview'
        db.create_table(u'market_treetreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('treet_purchase', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['market.TreetPurchase'], unique=True)),
        ))
        db.send_create_signal(u'market', ['TreetReview'])

        # Adding model 'TreetPurchase'
        db.create_table(u'market_treetpurchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('treet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['market.Treet'])),
            ('purchaser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purchaser', to=orm['auth.User'])),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seller', to=orm['auth.User'])),
            ('purchased_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('resolved_on', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'market', ['TreetPurchase'])


    def backwards(self, orm):
        # Deleting model 'TreetReview'
        db.delete_table(u'market_treetreview')

        # Deleting model 'TreetPurchase'
        db.delete_table(u'market_treetpurchase')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'market.treet': {
            'Meta': {'object_name': 'Treet'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'market.treetpurchase': {
            'Meta': {'object_name': 'TreetPurchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchased_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchaser'", 'to': u"orm['auth.User']"}),
            'resolved_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seller'", 'to': u"orm['auth.User']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'treet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['market.Treet']"})
        },
        u'market.treetreview': {
            'Meta': {'object_name': 'TreetReview'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'treet_purchase': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['market.TreetPurchase']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['market']