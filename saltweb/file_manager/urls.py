from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^file_upload/$', views.file_upload),
	url(r'^upload_script/$', views.uploadify_script),
	url(r'^upload_list/$', views.upload_list),
	url(r'^file_del/$', views.file_del),
	url(r'^file_send/$', views.file_send),
	url(r'^file_push/$', views.file_push),
]
