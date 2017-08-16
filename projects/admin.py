# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tech, Project

# Register your models here.
admin.site.register(Tech)
admin.site.register(Project)
