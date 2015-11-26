#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import os,json
from ssh_api import *
from saltweb.api import *

def file_upload(request):
	username,role_name,usergroup_name = get_session_user(request)
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

def upload_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	file_list = os.listdir(Local_Dir)
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,file_list)
        pt = p.pt()
        ppn = p.ppn()
        npn = p.npn()
        pn = p.pn()
        pl = p.pl()
        if page < 9:
                pr = p.pr()[0:9]
        elif int(pn) - page < 9:
                pr = p.pr()[int(pn)-9:int(pn)]
        else:
                pr = p.pr()[page-9:page+8]
	return render_to_response('file_manager/upload_list.html',locals())

def file_del(request):
	filename = request.POST.get('filename')
	try:
		r_filename = os.path.join(Local_Dir,filename)
		os.system('rm -rf %s' %r_filename)
		return HttpResponse('%s del success' %filename)
	except Exception as e:
		return HttpResponse('%s del failed,%s' %(filename,e))

def file_send(request):
	filename = request.POST.get('filename')
	try:
		local_filename = os.path.join(Local_Dir,filename)
		remote_filename = os.path.join(saltstack_remote_dir,filename)
		ret = s.send_file(local_filename,remote_filename)
	except Exception as e:
		ret = "%s send failed,%s" %(filename,e)
	return HttpResponse(ret)

def file_push(request):
	if request.method == "GET":
		username,role_name,usergroup_name = get_session_user(request)	
		remote_file_list = s.exec_command_list('ls %s' %saltstack_remote_dir)
	else:
		username,role_name,usergroup_name = get_session_user(request)
                remote_file_list = s.exec_command_list('ls %s' %saltstack_remote_dir)
		saltkey = request.POST.get('saltkey')
		remote_dir = request.POST.get('remote_dir')
		local_filename = request.POST.get('local_filename')
		salt_filename = "salt://upload/"+local_filename
		remote_filename = os.path.join(remote_dir,local_filename)
		ret = SALTAPI.salt_mod(saltkey,'cp.get_file',[salt_filename.strip(),remote_filename.strip()])['return'][0].items()
	return render_to_response('file_manager/file_push.html',locals())
