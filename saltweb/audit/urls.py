from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^cobbler_log/$', views.cobbler_log),
    url(r'^cobbler_log_del/$', views.cobbler_log_del),
    url(r'^login_log/$', views.login_log),
    url(r'^command_log/$', views.command_log),
]
