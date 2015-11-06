from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add_host/$', views.add_host),
    url(r'^host_list/$', views.host_list),
    url(r'^host_edit/$', views.host_edit),
    url(r'^host_del_ajax/$', views.host_del_ajax),
    url(r'^libvirt_manager/$', views.libvirt_manager),
    url(r'^libvirt_manager/virtual_info/$', views.virtual_info),
    url(r'^libvirt_manager/virtual_start/$', views.virtual_start),
    url(r'^libvirt_manager/virtual_stop/$', views.virtual_stop),
    url(r'^libvirt_manager/virtual_xmldown/$', views.virtual_xmldown),
]
