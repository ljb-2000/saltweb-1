# coding: utf8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from saltweb.api import *
from saltweb.dashboard import *
from user_manager.models import *
from perm.models import *
from audit.models import *
import json

@require_login
def index(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	print nav
    	weeks = list_week(7)
    	week_counts = list_week_count()
    	fun_counts = fun_count()
    	rows = list_jobs()
    	return render_to_response('index.html',locals())

def login(request):
    '''用户登入'''
    if request.session.get('username'):
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_filter = User.objects.filter(username=username)
        if user_filter:
            user = user_filter[0]
            if md5_crypt(password) == user.password:
                request.session['user_id'] = user.id
                user_filter.update(last_login=datetime.datetime.now())
		'''用户登录记录'''
		remote_ip = request.META['REMOTE_ADDR']
		LoginLog.objects.create(login_time=datetime.datetime.now(),username=username,ip=remote_ip)
                if user.role == 'SU':
                    request.session['role_id'] = 1
                else:
                    request.session['role_id'] = 0
                return HttpResponseRedirect('/')
            else:
                error = '密码错误，请重新输入'
        else:
            error = '用户不存在'
    return render_to_response('login.html',locals())

def logout(request):
    	request.session.delete()
    	return HttpResponseRedirect('/login')

@require_login
def jid_result(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	if request.method == 'GET':
		jid = request.GET.get('jid','')
		rows = get_jids(jid)
		if rows:
			'''取出返回值,并将json字符变成Python对象'''
			returns = json.loads(rows[0][0])
			if type(returns['return']) == dict:
				results_dict = returns
			else:
				results = returns
		else:
			error = "Jid无效,请检测是否正确"
	return render_to_response('jid_result.html',locals())

@require_login
def job_list_all(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	search = request.GET.get('search','')
	if search:
		results = list_job_search(search)
	else:
		results = list_job_all()
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
        pagenum = 10
        p = paging(page,pagenum,results)
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
	return render_to_response('job_list_all.html',locals())

@require_login
def job_list_failed(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
        search = request.GET.get('search','')
        if search:
                results = list_job_failed_search(search)
        else:
                results = list_job_failed()
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,results)
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
        return render_to_response('job_list_failed.html',locals())

@require_login
def job_list_state(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
        search = request.GET.get('search','')
        if search:
                results = list_job_state_search(search)
        else:
                results = list_job_state()
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,results)
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
        return render_to_response('job_list_state.html',locals())

@require_login
def job_list_highstate(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
        search = request.GET.get('search','')
        if search:
                results = list_job_highstate_search(search)
        else:
                results = list_job_highstate()
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,results)
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
        return render_to_response('job_list_highstate.html',locals())

def init_superuser(request):
	'''初始化超级用户'''
	if not request.GET.get('username',''):
		return HttpResponse('username is null')
	if not request.GET.get('password',''):
		return HttpResponse('password is null')
	username = request.GET.get('username')
	password = request.GET.get('password')
	try:
		u_obj = User.objects.filter(username=username)
		if u_obj:
			return HttpResponse('%s add failed,%s is exist' %(username,username))
		else:
                        User.objects.create(
                                username=username,
                                password=md5_crypt(password),
                                email='%s@example.com' %username,
                                role='SU',
                                is_active='1',
                                date_joined=datetime.datetime.now()
                        )
                        return HttpResponse('%s add success,pwd: %s' %(username,password))
	except Exception as e:
		return HttpResponse('add failed: %s' %e)
