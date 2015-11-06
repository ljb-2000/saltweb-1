from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^accepted_list/$', views.accepted_list),
    url(r'^unaccepted_list/$', views.unaccepted_list),
    url(r'^accept_key_ajax/$', views.accept_key_ajax),
    url(r'^delete_key_ajax/$', views.delete_key_ajax),
]
