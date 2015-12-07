from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^parent_menu_add/$', views.parent_menu_add),
    url(r'^parent_menu_list/$', views.parent_menu_list),
    url(r'^submenu_manager/$', views.submenu_manager),
    url(r'^submenu_del_ajax/$', views.submenu_del_ajax),
    url(r'^parentmenu_del_ajax/$', views.parentmenu_del_ajax),
]
