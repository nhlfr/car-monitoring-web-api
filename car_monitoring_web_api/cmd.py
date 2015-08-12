# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
from oslo.config import cfg
from wsgiref import simple_server

from car_monitoring_web_api import app
from car_monitoring_web_api.db.migration import cli as migration_cli


def db_manage():
    """Console script for managing database migrations."""
    parser = argparse.ArgumentParser('car-monitoring-db-manage')
    subparsers = parser.add_subparsers()

    version = subparsers.add_parser('version')
    version.set_defaults(func=migration_cli.do_version)

    upgrade = subparsers.add_parser('upgrade')
    upgrade.add_argument('revision', nargs='?')
    upgrade.set_defaults(func=migration_cli.do_upgrade)

    downgrade = subparsers.add_parser('downgrade')
    downgrade.add_argument('revision', nargs='?')
    downgrade.set_defaults(func=migration_cli.do_downgrade)

    stamp = subparsers.add_parser('stamp')
    stamp.add_argument('revision')
    stamp.set_defaults(func=migration_cli.do_stamp)

    revision = subparsers.add_parser('revision')
    revision.add_argument('-m', '--message')
    revision.add_argument('--autogenerate', action='store_true')
    revision.set_defaults(func=migration_cli.do_revision)

    config = migration_cli.get_alembic_config()
    parsed_args = parser.parse_args().__dict__
    func = parsed_args.pop('func')

    return func(config, **parsed_args)


def api():
    """Console script for serving API."""
    server = simple_server.make_server('0.0.0.0', 8080, app.get_app())
    server.serve_forever()
