#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import os,json

def file_upload(request):
	return render_to_response('file_manager/file_upload.html',locals())

def uploadify_script(request):  
    	'''uploadfify filename is Filedata'''
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	upload_dir = os.path.join(base_dir,'upload')
	if os.path.isdir(upload_dir):
		pass
	else:
		os.mkdir(upload_dir)
    	file_obj = request.FILES.get("Filedata",None)  
    	if file_obj:
		filename = file_obj.name
		upload_file = os.path.join(upload_dir,filename)
		f = open(upload_file,'wb+')
		for chunk in file_obj.chunks():
			f.write(chunk)
		f.close()
	return HttpResponse("upload success")
