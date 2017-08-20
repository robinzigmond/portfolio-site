"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from settings import MEDIA_ROOT
from projects import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.home),
    url(r"^about/$", views.about),
    url(r"^tech/$", views.techs),
    url(r"^tech/(?P<tech>.*)$", views.single_tech),
    url(r"^projects/$", views.portfolio),
    # url(r"^projects/using/(?P<tech>.*)$", views.projects_by_tech),
    url(r"^projects/(?P<name>.*)$", views.single_project),
    url(r"^cv/$", views.cv),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT})
]
