from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add_host/$', views.add_host),
    url(r'^host_list/$', views.host_list),
    url(r'^host_del_ajax/$', views.host_del_ajax),
    url(r'^libvirt_manager/$', views.libvirt_manager),
]
