#!/usr/bin/env python
from __future__ import with_statement

import os.path
import xmlrpclib
import pip

from fabric.api import local, settings
from fabric.contrib.console import confirm


def sync(static=False, reset=False):
    APPS_TO_WATCH = []
    if reset:
        local('python manage.py flush --noinput')
        local('python manage.py createsuperuser --username=saul --email=s.shanabrook@gmail.com')
        for app in APPS_TO_WATCH:
            local('python manage.py migrate {} --fake'.format(app))
        sync()
    else:
        local('python manage.py syncdb')
        with settings(warn_only=True):
            for app in APPS_TO_WATCH:
                if os.path.isfile(os.path.abspath(os.path.join(os.path.dirname(__file__), "{{ project_name }}", app, 'migrations/0001_initial.py'))):
                    local('python manage.py schemamigration %s --auto' % app)
                else:
                    local('python manage.py schemamigration %s --initial' % app)
            local('python manage.py migrate')
    if static:
        local('python manage.py collectstatic')