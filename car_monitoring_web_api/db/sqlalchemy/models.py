# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from oslo_db.sqlalchemy import models
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer


class MyBase(models.TimestampMixin, models.ModelBase):
    metadata = None

    id = Column(Integer, primary_key=True)
    value = Float()


class Speed(MyBase):
    __tablename__ = 'speed'


class RPM(MyBase):
    __tablename__ = 'rpm'
