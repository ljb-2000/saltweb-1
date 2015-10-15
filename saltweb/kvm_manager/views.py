#coding: utf-8

from django.db.models import  Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from kvm_manager.models import *
from saltweb.api import *

def add_host(request):
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

def host_list(request):
	search = request.GET.get('search')
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
	pl = p.pl()
	if page < 9:
		pr = p.pr()[0:9]
	elif int(pn) - page < 9:
		pr = p.pr()[int(pn)-9:int(pn)]
	else:
		pr = p.pr()[page-9:page+8]
	return render_to_response('kvm_manager/host_list.html',locals())

def host_del_ajax(request):
	ip = request.POST.get('ip')
	try:
		Host.objects.get(ip=ip).delete()
		ret = u'主机 %s 删除成功' %(ip)
	except Exception as e:
		ret = u'主机 %s 删除失败, %s' %(ip,e)
	return HttpResponse(ret)

def libvirt_manager(request):
	saltkey = request.GET.get('saltkey')
	saltapi_ret = SALTAPI.salt_mod(saltkey,'virt.vm_state').get('return')[0].get(saltkey)
	return render_to_response('kvm_manager/libvirt_manager.html',locals())
