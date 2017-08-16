# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    gitHubLink = models.URLField()
    activeLink = models.URLField(blank=True)
    techs = models.ManyToManyField(Tech, blank=True)

    def __unicode__(self):
        return self.name

