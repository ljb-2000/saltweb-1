#coding: utf-8

from django.db.models import  Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render_to_response
from kvm_manager.models import *
from saltweb.api import *
import json

@require_super_user
def add_host(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	if request.method == 'POST':
		saltkey = request.POST.get('saltkey')
		hostname = request.POST.get('hostname')
		ip = request.POST.get('ip')
		comment = request.POST.get('comment')
		try:
			'''insert host into db'''
			host = Host(
				saltkey = saltkey,
				hostname = hostname,
				ip = ip,
				comment = comment
			)
			host.save()
			ret = u'主机 %s--%s 添加成功' %(saltkey,ip)
		except Exception as e:
			error = u'主机 %s--%s 添加失败, %s' %(saltkey,ip,e)
	return render_to_response('kvm_manager/add_host.html',locals())

@require_login
def host_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	search = request.GET.get('search','')
	if search:
		hosts = Host.objects.filter(Q(saltkey__icontains=search) | Q(hostname__icontains=search) | Q(ip__icontains=search))
	else:
		hosts = Host.objects.all()
	'''分页'''
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
	pagenum = 10
	p = paging(page,pagenum,hosts)
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
	return render_to_response('kvm_manager/host_list.html',locals())

@require_super_user
def host_edit(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	if request.method == 'GET':
		ip = request.GET.get('ip')
		db_result = Host.objects.filter(ip=ip)[0]
		if db_result:
			saltkey = db_result.saltkey
			hostname = db_result.hostname
			ip = db_result.ip
			comment = db_result.comment
		return render_to_response('kvm_manager/host_edit.html',locals())
	else:
		saltkey = request.POST.get('saltkey')
		hostname = request.POST.get('hostname')
		ip = request.POST.get('ip')
		comment = request.POST.get('comment')
		try:
			Host.objects.filter(ip=ip).update(
				saltkey=saltkey,
				hostname=hostname,
				ip=ip,
				comment=comment
			)
			ret = u'update success'
		except Exception as e:
			error = u'update failed: %s' % e
		return render_to_response('kvm_manager/host_edit.html',locals())

@require_super_user
def host_del_ajax(request):
	ip = request.POST.get('ip')
	try:
		Host.objects.get(ip=ip).delete()
		ret = u'主机 %s 删除成功' %(ip)
	except Exception as e:
		ret = u'主机 %s 删除失败, %s' %(ip,e)
	return HttpResponse(ret)

@require_login
def libvirt_manager(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	saltkey = request.GET.get('saltkey')
	saltapi_ret = SALTAPI.salt_mod(saltkey,'virt.vm_state').get('return')[0].get(saltkey)
	return render_to_response('kvm_manager/libvirt_manager.html',locals())

@require_login
def virtual_info(request):
	saltkey = request.GET.get('saltkey','')
	v_name = request.GET.get('v_name','')
	try:
		saltapi_ret = json.dumps(SALTAPI.salt_mod(saltkey,'virt.vm_info',v_name)["return"][0][saltkey][v_name],indent=4)
	except Exception as e:
		saltapi_ret = "request salt api failed: %s" % e
	return HttpResponse(saltapi_ret)

@require_super_user
def virtual_start(request):
	saltkey = request.POST.get('saltkey','')
	v_name = request.POST.get('v_name','')
	try:
		saltapi_ret = SALTAPI.salt_mod(saltkey,'virt.start',v_name)['return'][0][saltkey]
	except Exception as e:
		saltapi_ret = 'request salt api failed: %s' % e
	return HttpResponse(saltapi_ret)

@require_super_user
def virtual_stop(request):
	saltkey = request.POST.get('saltkey','')
	v_name = request.POST.get('v_name','')
	try:
		saltapi_ret = SALTAPI.salt_mod(saltkey,'virt.stop',v_name)['return'][0][saltkey]
	except Exception as e:
		saltapi_ret = 'request salt api failed: %s' % e
	return HttpResponse(saltapi_ret)

@require_login
def virtual_xmldown(request):
	saltkey = request.GET.get('saltkey','')
	v_name = request.GET.get('v_name','')
	saltapi_ret = SALTAPI.salt_mod(saltkey,'virt.get_xml',v_name)['return'][0][saltkey]
	response = StreamingHttpResponse(saltapi_ret)
	response['Content-type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename=%s.xml' % v_name
	return response
