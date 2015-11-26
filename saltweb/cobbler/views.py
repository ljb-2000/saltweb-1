#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from cobbler_api import *
from saltweb.api import paging,get_session_user
from cobbler.models import *
import datetime
#import virtinst.util

def install(request):
	username,role_name,usergroup_name = get_session_user(request)
	if request.method == 'GET':
		profile_list = u_cobbler_api.seach_profile()
		#mac = virtinst.util.randomMAC(type="qemu")
	else:
		profile_list = u_cobbler_api.seach_profile()
		hostname = request.POST.get('hostname').strip()
		interface = request.POST.get('interface').strip()
		ip = request.POST.get('ip').strip()
		gateway = request.POST.get('gateway').strip()
		dns = request.POST.get('dns').strip()
		mac = request.POST.get('mac').strip()
		profile = request.POST.get('profile').strip()
		ret = u_cobbler_api.add_system(hostname,ip,interface,gateway,mac,dns,profile)
		if ret == "success":
			result = u"host: %s添加成功" %hostname
			'''add log into cobbler_log'''
			Cobbler_Log.objects.create(
				hostname=hostname,
				interface=interface,
				ip=ip,
				gateway=gateway,
				dns=dns,
				mac=mac,
				profile=profile,
				user=username,
				date_joined=datetime.datetime.now()
			)
		else:
			error = ret
	return render_to_response('cobbler/install.html',locals())

def install_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	system_list = u_cobbler_api.seach_system()
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,system_list)
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
	return render_to_response('cobbler/install_list.html',locals())

def cobbler_system_del(request):
	system_name = request.POST.get('system_name')
	ret = u_cobbler_api.del_system(system_name)
	if ret == 'success':
		result = u"system: %s删除成功" %system_name
	else:
		result = ret
	return HttpResponse(result)
