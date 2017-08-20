# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.db.models.functions import Lower
import models

# Create your views here.
def home(request):
    techs = models.Tech.objects.all().order_by(Lower("name"))
    for tech in techs:
        tech.formatted_name = tech.name.lower().replace(" ", "-").replace(".", "")
    return render(request, "home.html", {"active": "home", "techlist": techs})


def about(request):
    return render(request, "about.html", {"active": "about"})


def techs(request):
    techs = models.Tech.objects.all().order_by("-skill_level")
    for tech in techs:
        tech.formatted_name = tech.name.lower().replace(" ", "-").replace(".", "")
        tech.skill_level_times_ten = 10*tech.skill_level
    return render(request, "techs.html", {"active": "techs", "techs": techs})


def portfolio(request):
    projects = models.Project.objects.all()
    for project in projects:
        project.formatted_name = project.name.lower().replace(" ", "-")
    return render(request, "portfolio.html", {"active": "portfolio", "projects": projects})


def single_tech(request, tech):
    techs = models.Tech.objects.all().order_by(Lower("name"))
    tech_name = None
    for technology in techs:
        technology.formatted_name = technology.name.lower().replace(" ", "-").replace(".", "")
        technology.skill_level_times_ten = 10*technology.skill_level
        if technology.name.lower().replace(".", "") == tech.replace("-", " "):
            tech_name = technology
    projects = models.Project.objects.filter(techs__name=tech_name)
    if tech_name is None or not projects:
        raise Http404("Sorry, no projects found using that tech")
    for project in projects:
        project.formatted_name = project.name.lower().replace(" ", "-")
    return render(request, "tech.html", {"active": "techs", "projects": projects, "tech": tech_name})


def single_project(request, name):
    projects = models.Project.objects.all()
    project = None
    for site in projects:
        if site.name.lower() == name.replace("-", " "):
            project = site
    if project is None:
        raise Http404("Sorry, project not found")
    techs_used = project.techs.all().order_by(Lower("name"))
    for tech in techs_used:
        tech.formatted_name = tech.name.lower().replace(" ", "-").replace(".", "")
    return render(request, "project.html", {"active": "portfolio", "project": project, "techs": techs_used})
