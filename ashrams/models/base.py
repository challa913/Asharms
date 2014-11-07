__author__ = 'challa'

from django.db import models
from django.utils import timezone


class Base(models.Model):
    created_date = models.DateTimeField('date created', default=timezone.now())
    modified_date = models.DateTimeField('date modified', default=timezone.now())

    class Meta:
        abstract = True
