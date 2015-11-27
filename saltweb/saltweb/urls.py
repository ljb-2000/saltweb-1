"""saltweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^jid_result/$', views.jid_result),
    url(r'^job_list_all/$', views.job_list_all),
    url(r'^job_list_failed/$', views.job_list_failed),
    url(r'^job_list_state/$', views.job_list_state),
    url(r'^job_list_highstate/$', views.job_list_highstate),
    url(r'^asset/', include('asset.urls')),
    url(r'^kvm_manager/', include('kvm_manager.urls')),
    url(r'^user_manager/', include('user_manager.urls')),
    url(r'^salt_module/', include('salt_module.urls')),
    url(r'^saltkey_manager/', include('saltkey_manager.urls')),
    url(r'^cobbler/', include('cobbler.urls')),
    url(r'^file_manager/', include('file_manager.urls')),
    url(r'^audit/', include('audit.urls')),
    url(r'^perm/', include('perm.urls')),
]
