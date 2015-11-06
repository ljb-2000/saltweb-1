from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^file_upload/$', views.file_upload),
	url(r'^upload_script/$', views.uploadify_script),
]
