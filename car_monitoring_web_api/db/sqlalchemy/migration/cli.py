# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from alembic import command
from alembic import config as alembic_config


def do_version(config):
    return command.current(config)


def do_upgrade(config, revision=None):
    # Parser already shoud have a "revision" value, even it it's None,
    # therefore real default value is set here
    if revision is None:
        revision = 'head'
    return command.upgrade(config, revision)


def do_downgrade(config, revision=None):
    return command.downgrade(config, revision)


def do_stamp(config, revision=None):
    return command.stamp(config, revision)


def do_revision(config, message=None, autogenerate=False):
    return command.revision(config, message, autogenerate)


def get_alembic_config():
    config = alembic_config.Config(os.path.join(os.path.dirname(__file__),
                                                'alembic.ini'))
    # config.set_main_option('sqlalchemy.url', settings.FCONN)

    return config
