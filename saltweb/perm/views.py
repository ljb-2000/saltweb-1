#coding: utf-8

from django.db.models import  Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from perm.models import *
from saltweb.api import *

@require_super_user
def parent_menu_add(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	if request.method == 'POST':
		name = request.POST.get('name')
		try:
			Parent_Menu.objects.create(name=name)
			result = u'父菜单: %s添加成功' %name
		except Exception as e:
			error = u'父菜单: %s添加失败,%s' %(name,e)
	return render_to_response('perm/parent_menu_add.html',locals())
			
@require_super_user
def parent_menu_list(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
        search = request.GET.get('search','')
        if search:
                menus = Parent_Menu.objects.filter(Q(name__icontains=search))
        else:
                menus = Parent_Menu.objects.all()
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,menus)
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
        return render_to_response('perm/parent_menu_list.html',locals())

@require_super_user
def submenu_manager(request):
	username,role_name,usergroup_name = get_session_user(request)
	session_role_id = request.session['role_id']
	nav = perm_nav(request)
	if request.method == 'GET':
		parentmenu_name = request.GET.get('name')
		p = Parent_Menu.objects.get(name=parentmenu_name)
		submenus = p.sub_menu_set.all()
        	'''分页'''
        	try:
                	page = int(request.GET.get('page','1'))
        	except ValueError:
                	page = 1
        	pagenum = 10
        	p = paging(page,pagenum,submenus)
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
		return render_to_response('perm/submenu_manager.html',locals())
	else:
		parentmenuname = request.POST.get('parentmenuname')
		submenuname = request.POST.get('submenuname')
		suburl = request.POST.get('suburl')
		p_obj = Parent_Menu.objects.get(name=parentmenuname)
		Sub_Menu.objects.create(name=submenuname,parent_menu=p_obj,url=suburl)
		return HttpResponseRedirect('/perm/submenu_manager/?name=%s' %parentmenuname)

@require_super_user
def submenu_del_ajax(request):
	submenu_name = request.POST.get('submenu_name')
	try:
		sub_obj = Sub_Menu.objects.get(name=submenu_name)
		sub_obj.delete()
		return HttpResponse(u'子菜单删除成功')
	except Exception as e:
		return HttpResponse(u"子菜单删除失败,%s" %e)

@require_super_user
def parentmenu_del_ajax(request):
	parentmenu_name = request.POST.get('parentmenu_name')
	try:
		parentmenu_obj = Parent_Menu.objects.get(name=parentmenu_name)
		parentmenu_obj.delete()
                return HttpResponse(u'父菜单删除成功')
        except Exception as e:
                return HttpResponse(u"父菜单删除失败,%s" %e)
