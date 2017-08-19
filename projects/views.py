# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models

# Create your views here.
def home(request):
    tech = models.Tech.objects.all()
    return render(request, "home.html", {"active": "home", "techlist": tech})
