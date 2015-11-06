from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^cobbler_log/$', views.cobbler_log),
    url(r'^cobbler_log_del/$', views.cobbler_log_del),
]
