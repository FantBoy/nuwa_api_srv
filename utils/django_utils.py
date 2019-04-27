# -*- coding: utf-8 -*-
import itertools
import os
import sys

import django

def setup_django():
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'nuwa_api_srv.settings'

    # https://docs.djangoproject.com/fr/1.7/releases/1.7/#standalone-scripts
    if django.VERSION >= (1, 7):
        django.setup()


def model_to_dict(instance, fields=None, exclude=None):
    """
    通过一个 Django 的 model 实例生成一个词典，词典的 key 为 instance 的 field 名，
    value 为该 field 的值。

    Returns a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, only the named
    fields will be included in the returned dict.

    ``exclude`` is an optional list of field names. If provided, the named
    fields will be excluded from the returned dict, even if they are listed in
    the ``fields`` argument.
    """
    from django.forms import model_to_dict
    data = model_to_dict(instance, fields, exclude)

    opts = instance._meta
    for f in itertools.chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if not getattr(f, 'editable', False):
            data[f.name] = f.value_from_object(instance)

    return data
