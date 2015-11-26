from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add_host/$', views.add_host),
    url(r'^add_host_service/$', views.add_host_service),
    url(r'^add_network/$', views.add_network),
    url(r'^add_storage/$', views.add_storage),
    url(r'^host_list/$', views.host_list),
    url(r'^network_list/$', views.network_list),
    url(r'^storage_list/$', views.storage_list),
    url(r'^host_del_ajax/$', views.host_del_ajax),
    url(r'^network_del_ajax/$', views.network_del_ajax),
    url(r'^storage_del_ajax/$', views.storage_del_ajax),
]
