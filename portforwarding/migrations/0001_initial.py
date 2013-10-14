# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Portforwarded'
        db.create_table(u'portforwarding_portforwarded', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server_host', self.gf('django.db.models.fields.related.ForeignKey')(related_name='portstoforward', to=orm['servers.Server'])),
            ('server_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='portsforwared', to=orm['servers.Server'])),
            ('port_from', self.gf('django.db.models.fields.IntegerField')()),
            ('port_to', self.gf('django.db.models.fields.IntegerField')()),
            ('protocol', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal(u'portforwarding', ['Portforwarded'])


    def backwards(self, orm):
        # Deleting model 'Portforwarded'
        db.delete_table(u'portforwarding_portforwarded')


    models = {
        u'portforwarding.portforwarded': {
            'Meta': {'object_name': 'Portforwarded'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'port_from': ('django.db.models.fields.IntegerField', [], {}),
            'port_to': ('django.db.models.fields.IntegerField', [], {}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'server_host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'portstoforward'", 'to': u"orm['servers.Server']"}),
            'server_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'portsforwared'", 'to': u"orm['servers.Server']"})
        },
        u'servers.server': {
            'Meta': {'object_name': 'Server'},
            'external_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_vm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keymanger_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ssh_connection_string': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vm_host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servers.Server']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portforwarding']