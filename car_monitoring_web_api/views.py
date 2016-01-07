# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pyramid.response as pyramid_response
import pyramid.view as pyramid_view


class BaseView(object):
    
    def __init__(self, request):
        self.request = request


@pyramid_view.view_defaults(route_name='speed')
class SpeedView(BaseView):

    @pyramid_view.view_config(request_method='GET', renderer='json')
    def get(self):
        return []

    @pyramid_view.view_config(request_method='POST', renderer='json')
    def post(self):
        pass


@pyramid_view.view_defaults(route_name='rpm')
class RPMView(BaseView):

    @pyramid_view.view_config(request_method='GET', renderer='json')
    def get(self):
        return []

    @pyramid_view.view_config(request_method='POST', renderer='json')
    def post(self):
        pass
