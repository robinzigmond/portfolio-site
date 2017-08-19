# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    gitHubLink = models.URLField()
    activeLink = models.URLField(blank=True)
    techs = models.ManyToManyField(Tech, blank=True)
    screenshot = models.ImageField(upload_to="screenshots", null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
