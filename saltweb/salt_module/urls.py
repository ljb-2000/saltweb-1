from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add_modules/$', views.add_modules),
    url(r'^module_list/$', views.module_list),
    url(r'^module_exec/$', views.module_exec),
    url(r'^module_del_ajax/$', views.module_del_ajax),
    url(r'^module_exec_ajax/$', views.module_exec_ajax),
]
