# -*- coding: utf-8 -*-
from __future__ import with_statement

from fabric.api import *

from conf.fab_settings import *

REQ_TXT = 'requirements/base.txt'


def pull():
    sudo('git pull')


def install_packages():
    sudo(f'pip install -U pip')
    sudo(f'pip install -r {REQ_TXT}')


def collect_static():
    sudo('python manage.py collectstatic --noinput')


def migrate():
    sudo('python manage.py migrate')


def touch():
    sudo('touch ./srv/prod/wsgi.py')


def deploy():
    with cd(PROJECT_ROOT):
        with prefix('source ./venv/bin/activate'):
            pull()
            install_packages()
            collect_static()
            migrate()
            touch()
