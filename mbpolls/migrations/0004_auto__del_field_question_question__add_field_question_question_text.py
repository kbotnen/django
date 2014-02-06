# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.question'
        db.delete_column(u'mbpolls_question', 'question')

        # Adding field 'Question.question_text'
        db.add_column(u'mbpolls_question', 'question_text',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Question.question'
        db.add_column(u'mbpolls_question', 'question',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)

        # Deleting field 'Question.question_text'
        db.delete_column(u'mbpolls_question', 'question_text')


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
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mbpolls']