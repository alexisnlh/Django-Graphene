"""core URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin_django/', admin.site.urls)]         # Web del administrador de Django

urlpatterns += [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]
