#coding: utf-8
from django.db.models import  Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from salt_module.models import *
from saltweb.api import *
import json

def add_modules(request):
	username,role_name,usergroup_name = get_session_user(request)
	if request.method == 'POST':
		module_name = request.POST.get('module_name')
		module_info = request.POST.get('module_info')
		args_info = request.POST.get('args_info')
		try:
			add = Module(
				module_name = module_name,
				module_info = module_info,
				args_info = args_info
			)
			add.save()
			result = u'模块: %s添加成功' %module_name
		except Exception as e:
			error = u'模块: %s添加失败: %s' %(module_name,e)
	return render_to_response('salt_module/add_modules.html',locals())

def module_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	search = request.GET.get('search','')
        if search:
                modules = Module.objects.filter(Q(module_name__icontains=search))
        else:
                modules = Module.objects.all()
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,modules)
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
	return render_to_response('salt_module/module_list.html',locals())

def module_exec(request):
        username,role_name,usergroup_name = get_session_user(request)
        if request.method == 'GET':
		module_name = request.GET.get('module_name')
		ret = Module.objects.get(module_name=module_name)
	return render_to_response('salt_module/module_exec.html',locals())

def module_del_ajax(request):
	module_name = request.POST.get('module_name')
	try:
		Module.objects.get(module_name=module_name).delete()
		ret = u'模块: %s删除成功' %module_name
	except Exception as e:
		ret = u'模块: %s删除失败: %s' %(module_name,e)
	return HttpResponse(ret)

def module_exec_ajax(request):
	saltkey = request.POST.get('saltkey')
	module_name = request.POST.get('module_name')
	args = request.POST.get('args').split(',')
	ret = SALTAPI.salt_mod(saltkey,module_name,args)['return'][0]
	print ret
	return HttpResponse(json.dumps(ret))
