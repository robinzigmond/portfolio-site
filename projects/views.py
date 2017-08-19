# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models

# Create your views here.
def home(request):
    tech = models.Tech.objects.all()
    return render(request, "home.html", {"active": "home", "techlist": tech})


def about(request):
    return render(request, "about.html", {"active": "about"})


def techs(request):
    return render(request, "techs.html", {"active": "techs"})


def portfolio(request):
    projects = models.Project.objects.all()
    return render(request, "portfolio.html", {"active": "portfolio", "projects": projects})


def cv(request):
    return render(request, "cv.html", {"active": "cv"})
