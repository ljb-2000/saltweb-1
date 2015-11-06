from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^install/$', views.install),
    url(r'^install_list/$', views.install_list),
    url(r'^cobbler_system_del/$', views.cobbler_system_del),
]
