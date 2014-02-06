# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'mbpolls_poll')

        # Adding model 'Question'
        db.create_table(u'mbpolls_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'mbpolls', ['Question'])

        # Deleting field 'Choice.poll'
        db.delete_column(u'mbpolls_choice', 'poll_id')

        # Adding field 'Choice.question'
        db.add_column(u'mbpolls_choice', 'question',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['mbpolls.Question']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'mbpolls_poll', (
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mbpolls', ['Poll'])

        # Deleting model 'Question'
        db.delete_table(u'mbpolls_question')

        # Adding field 'Choice.poll'
        db.add_column(u'mbpolls_choice', 'poll',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['mbpolls.Poll']),
                      keep_default=False)

        # Deleting field 'Choice.question'
        db.delete_column(u'mbpolls_choice', 'question_id')


    models = {
        u'mbpolls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mbpolls.Question']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mbpolls.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mbpolls']