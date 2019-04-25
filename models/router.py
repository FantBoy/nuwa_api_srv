# -*- coding=utf-8 -*-
from __future__ import unicode_literals

class DatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'nodetube_app':
            return 'default'
        if model._meta.app_label == 'packagetube_app':
            return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'nodetube_app':
            return 'default'
        if model._meta.app_label == 'packagetube_app':
            return 'default'
