from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^user_add/$', views.user_add),
    url(r'^usergroup_add/$', views.usergroup_add),
    url(r'^user_list/$', views.user_list),
    url(r'^usergroup_list/$', views.usergroup_list),
    url(r'^user_del_ajax/$', views.user_del_ajax),
    url(r'^usergroup_del_ajax/$', views.usergroup_del_ajax),
    url(r'^user_edit/$', views.user_edit),
    url(r'^usergroup_edit/$', views.usergroup_edit),
    url(r'^g_user_list_ajax/$', views.g_user_list_ajax),
    url(r'^user_perm_edit/$', views.user_perm_edit),
]
