# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pyramid import config as pyramid_config

from car_monitoring_web_api import views


def get_app():
    """App object with routes."""
    config = pyramid_config.Configurator()

    config.add_route('speed', '/speed')
    config.add_route('rpm', '/rpm')

    config.scan(views)

    app = config.make_wsgi_app()

    return app
