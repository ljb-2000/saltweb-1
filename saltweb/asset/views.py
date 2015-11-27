#coding: utf-8

from django.db.models import  Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from asset.models import *
from saltweb.api import *

@require_super_user
def add_host(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav_name = "asset"
        if request.method == 'POST':
                saltkey = request.POST.get('saltkey')
                hostname = request.POST.get('hostname')
                ip = request.POST.get('ip')
                kernel = request.POST.get('kernel')
                os = request.POST.get('os')
                cpunum = request.POST.get('cpunum')
                cputype = request.POST.get('cputype')
                memory = request.POST.get('memory')
                disk = request.POST.get('disk')
                comment = request.POST.get('comment')
                try:
                        host = Host(
                                saltkey=saltkey,
                                hostname=hostname,
                                ip=ip,
                                kernel=kernel,
                                os=os,
                                cpunum=cpunum,
                                cputype=cputype,
                                memory=memory,
                                disk=disk,
                                comment=comment
                        )
                        host.save()
                        ret = u'%s -- %s添加成功' %(saltkey,ip)
                except Exception as e:
                        error = u'%s -- %s添加失败: %s' %(saltkey,ip,e)
        return render_to_response('asset/add_host.html',locals())

@require_super_user
def add_network(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav_name = "asset"
        if request.method == 'POST':
                ip = request.POST.get('ip')
                device = request.POST.get('device')
                comment = request.POST.get('comment')
                try:
                        network = Network(
                                ip=ip,
                                device=device,
                                comment=comment
                        )
                        network.save()
                        ret = u'%s -- %s添加成功' %(device,ip)
                except Exception as e:
                        error = u'%s -- %s添加失败: %s' %(device,ip,e)
        return render_to_response('asset/add_network.html',locals())

@require_super_user
def add_storage(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav_name = "asset"
        if request.method == 'POST':
                ip = request.POST.get('ip')
                device = request.POST.get('device')
                comment = request.POST.get('comment')
                try:
                        storage = Storage(
                                ip=ip,
                                device=device,
                                comment=comment
                        )
                        storage.save()
                        ret = u'%s -- %s添加成功' %(device,ip)
                except Exception as e:
                        error = u'%s -- %s添加失败: %s' %(device,ip,e)
        return render_to_response('asset/add_storage.html',locals())

@require_login
def host_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	nav_name = "asset"
	session_role_id = request.session['role_id']
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
        return render_to_response('asset/host_list.html',locals())

@require_login
def network_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav_name = "asset"
        search = request.GET.get('search','')
        if search:
                network = Network.objects.filter(Q(device__icontains=search) | Q(ip__icontains=search))
        else:
                network = Network.objects.all()
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,network)
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
        return render_to_response('asset/network_list.html',locals())

@require_login
def storage_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav_name = "asset"
        search = request.GET.get('search','')
        if search:
                storage = Storage.objects.filter(Q(device__icontains=search) | Q(ip__icontains=search))
        else:
                storage = Storage.objects.all()
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,storage)
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
        return render_to_response('asset/storage_list.html',locals())

@require_super_user
def host_del_ajax(request):
	ip = request.POST.get('ip')
	try:
		Host.objects.get(ip=ip).delete()
		ret = u'主机 %s 删除成功' %(ip)
	except Exception as e:
		ret = u'主机 %s 删除失败, %s' %(ip,e)
	return HttpResponse(ret)

@require_super_user
def network_del_ajax(request):
	ip = request.POST.get('ip')
	try:
		Network.objects.get(ip=ip).delete()
		ret = u'主机 %s 删除成功' %(ip)
	except Exception as e:
		ret = u'主机 %s 删除失败, %s' %(ip,e)
	return HttpResponse(ret)

@require_super_user
def storage_del_ajax(request):
	ip = request.POST.get('ip')
	try:
		Storage.objects.get(ip=ip).delete()
		ret = u'主机 %s 删除成功' %(ip)
	except Exception as e:
		ret = u'主机 %s 删除失败, %s' %(ip,e)
	return HttpResponse(ret)

def add_host_service(request):
	'''添加host接口'''
	if request.method == "GET":
		return HttpResponse("Error: Please Use Post Method")
	else:
		if not request.POST.get("saltkey",""):
			return HttpResponse("saltkey is null")
		if not request.POST.get("hostname",""):
			return HttpResponse("hostname is null")
		if not request.POST.get("ip",""):
			return HttpResponse("ip is null")
		if not request.POST.get("kernel",""):
			return HttpResponse("kernel is null")
		if not request.POST.get("os",""):
			return HttpResponse("os is null")
		if not request.POST.get("cpunum",""):
			return HttpResponse("cpunum is null")
		if not request.POST.get("cputype",""):
			return HttpResponse("cputype is null")
		if not request.POST.get("memory",""):
			return HttpResponse("memory is null")
		if not request.POST.get("disk",""):
			return HttpResponse("disk is null")
		saltkey = request.POST.get("saltkey")	
		hostname = request.POST.get("hostname")	
		ip = request.POST.get("ip")	
		kernel = request.POST.get("kernel")	
		os = request.POST.get("os")	
		cpunum = request.POST.get("cpunum")	
		cputype = request.POST.get("cputype")	
		memory = request.POST.get("memory")
		disk = request.POST.get("disk")
		comment = request.POST.get("comment","")
		selected = Host.objects.filter(ip=ip)
		if selected:
			'''如果存在记录'''
			selected.update(
				saltkey=saltkey,
				hostname=hostname,
				kernel=kernel,
				os=os,
				cpunum=cpunum,
				cputype=cputype,
                                memory=memory,
                                disk=disk,
                                comment=comment
			)
			return HttpResponse("update host success")
		else:
			host = Host(
				saltkey=saltkey,
				hostname=hostname,
				ip=ip,
				kernel=kernel,
				os=os,
				cpunum=cpunum,
				cputype=cputype,
				memory=memory,
				disk=disk,
				comment=comment
			)
			host.save()
			return HttpResponse("add host success")
	
