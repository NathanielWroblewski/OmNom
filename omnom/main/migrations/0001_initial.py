# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PickupRequest'
        db.create_table(u'main_pickuprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requests', to=orm['auth.User'])),
            ('is_fulfilled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fulfilled_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fulfilled_requests', to=orm['auth.User'])),
            ('is_picked_up', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expiry', self.gf('django.db.models.fields.IntegerField')(default=24)),
        ))
        db.send_create_signal(u'main', ['PickupRequest'])

        # Adding model 'Feedback'
        db.create_table(u'main_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pickup_request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.PickupRequest'])),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks_given', to=orm['auth.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks_received', to=orm['auth.User'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('feedback', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'PickupRequest'
        db.delete_table(u'main_pickuprequest')

        # Deleting model 'Feedback'
        db.delete_table(u'main_feedback')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks_given'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pickup_request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.PickupRequest']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks_received'", 'to': u"orm['auth.User']"})
        },
        u'main.pickuprequest': {
            'Meta': {'object_name': 'PickupRequest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expiry': ('django.db.models.fields.IntegerField', [], {'default': '24'}),
            'fulfilled_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fulfilled_requests'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_picked_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['main']