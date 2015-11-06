#coding: utf-8

from django.db.models import  Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from saltweb.api import paging,get_session_user
from cobbler.models import *

def cobbler_log(request):
	username,role_name,usergroup_name = get_session_user(request)
        search = request.GET.get('search','')
        if search:
                cobbler_list = Cobbler_Log.objects.filter(Q(hostname__icontains=search) | Q(user__icontains=search)).order_by('-date_joined')
        else:
                cobbler_list = Cobbler_Log.objects.all().order_by('-date_joined')
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,cobbler_list)
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
	return render_to_response('audit/cobbler_log.html',locals())

def cobbler_log_del(request):
	id = request.POST.get('id')
	try:
		Cobbler_Log.objects.get(id=id).delete()
		ret = u'记录删除成功'
	except Exception as e:
                ret = u'记录 删除失败: %s' %(e)
        return HttpResponse(ret)
	
