# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
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
    for project in projects:
        project.formatted_name = project.name.lower().replace(" ", "-")
    return render(request, "portfolio.html", {"active": "portfolio", "projects": projects})


def single_project(request, name):
    projects = models.Project.objects.all()
    project = None
    for site in projects:
        if site.name.lower() == name.replace("-", " "):
            project = site
    if project is None:
        raise Http404("Sorry, project not found")
    techs_used = project.techs.all()
    return render(request, "project.html", {"active": "portfolio", "project": project, "techs": techs_used})


def cv(request):
    return render(request, "cv.html", {"active": "cv"})
