# coding: utf-8
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
import urllib,urllib2
import json
import os
import hashlib
import random
import datetime
import ConfigParser
from user_manager.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))

# mail info
MAIL_FROM = config.get('mail', 'mail_from')

SALT_URL = config.get('salt-api', 'salt_url')
SALT_USERNAME = config.get('salt-api', 'salt_username') 
SALT_PASSWORD = config.get('salt-api','salt_password')

class SaltApi(object):
	__token = ''

	def __init__(self,url,username,password):
		self.__url = url
		self.__username = username
		self.__password = password

	def get_token(self):
		''' user login and get token id'''
		params = {'eauth' : 'pam', 'username' : self.__username, 'password' : self.__password}
		headers = {'Accept' : 'application/json'}
		args = urllib.urlencode(params)
		url = self.__url.rstrip('/')+'/login'
		req = urllib2.Request(url,args,headers)
		response = urllib2.urlopen(req).read()
		ret = json.loads(response)
		self.__token = ret['return'][0]['token'] 
	
	def postRequest(self,params,*args):
		url = self.__url.rstrip('/')
		headers = {'X-Auth-Token' : self.__token, 'Accept' : 'application/json'}
		if args:
			r_args = urllib.urlencode(params)+'&'+urllib.urlencode({'arg':args[0]},doseq=True)
		else:
			r_args = urllib.urlencode(params)
		req = urllib2.Request(url,r_args,headers)
		response = urllib2.urlopen(req).read()
		return json.loads(response)
		
		
	def list_all_key(self):
		self.get_token()
		params = {'client' : 'wheel' , 'fun': 'key.list_all'}
		ret = self.postRequest(params)
		return ret

	def delete_key(self,key):
		self.get_token()
		params = {'client': 'wheel', 'fun': 'key.delete', 'match': key}
		ret = self.postRequest(params)
		return ret['return'][0]['data']['success']

	def accept_key(self,key):
		'''add saltstack key,return True'''
		self.get_token()
		params = {'client': 'wheel', 'fun': 'key.accept', 'match': key}
		ret = self.postRequest(params)
		return ret['return'][0]['data']['success']

	def lookup_jid(self,jid):
		self.get_token()
		params = {'client' : 'runner' , 'fun' : 'jobs.lookup_jid' , 'jid' : jid}
		ret = self.postRequest(params)
		return ret

	def salt_mod(self,key,mod_name,*args):
		'''Usage: SALTAPI.salt_mod('test_v6_lvs0*','cp.get_file',['salt://aa','/tmp/aa'])'''
		'''return: {u'return': [{u'test_v6_lvs02': u'/tmp/aa', u'test_v6_lvs01': u'/tmp/aa'}]}'''
		self.get_token()
		params = {'client' : 'local', 'tgt': key, 'fun': mod_name}
		ret = self.postRequest(params,*args)
		return ret

SALTAPI = SaltApi(SALT_URL,SALT_USERNAME,SALT_PASSWORD)

class paging():
	'''分页函数'''
        def __init__(self,page,pagenum,select_result):
                self.page = int(page)
                self.pagenum = int(pagenum)
                self.select_result = select_result
                self.p = Paginator(self.select_result,self.pagenum)

        def pt(self):
                '''共有多少条数据'''
                return self.p.count

        def pn(self):
                '''总页数'''
                return self.p.num_pages

        def pr(self):
                '''获取页码列表'''
                return self.p.page_range

        def pl(self):
                '''第page页的数据列表'''
                return self.p.page(self.page).object_list

        def pp(self):
                '''是否有上一页'''
                return self.p.page(self.page).has_previous()

        def np(self):
                '''是否有下一页'''
                return self.p.page(self.page).has_next()

        def ppn(self):
                '''上一页页码号'''
                if self.page <= 1:
                        return '1'
                else:
                        return self.p.page(self.page).previous_page_number()

        def npn(self):
                '''下一页页码号'''
                if self.p.page(self.page).has_next() == False:
                        return self.page
                else:
                        return self.p.page(self.page).next_page_number()

def require_login(func):
	'''要求登入的装饰器'''
	def _deco(request,*args,**kwargs):
		if not request.session.get('user_id'):
            		return HttpResponseRedirect('/login')
        	return func(request,*args,**kwargs)
    	return _deco

def require_super_user(func):
	'''要求登入的用户是super用户,superuser session_role_id=1 other session_role_id=0'''
	def _deco(request,*args,**kwargs):
        	if not request.session.get('user_id'):
            		return HttpResponseRedirect('/login')

        	if request.session.get('role_id',0) != 1:
            		return HttpResponseRedirect('/')
        	return func(request,*args,**kwargs)
    	return _deco

def gen_rand_pwd(num):
	'''生成随机密码,num为密码位数'''
	seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pass_list = []
	for i in range(num):
        	pass_list.append(random.choice(seed))
    	passwd = ''.join(pass_list)
    	return passwd

def md5_crypt(string):
	'''加密用户密码入数据库'''
	return hashlib.new('md5',string).hexdigest()

def user_usergroup(uid):
	'''根据uid查询对应的用户组'''
	usergroup_list = []
	user = User.objects.filter(id=uid)
	if user:
		user = user[0]
		group_list = user.group.all()
		for u_g in group_list:
			usergroup_list.append(u_g.name)
	return usergroup_list

def get_session_user(request):
	'''现在在左侧导航栏的用户信息'''
	user_id = request.session.get('user_id',0)
	user = User.objects.filter(id=user_id)
	if user:
		user = user[0]
		username = user.username
		role = user.role
		usergroup = user_usergroup(user_id)
		if role == 'SU':
			role_name = u'超级管理员'
		else:
			role_name = u'普通用户'
		usergroup_name = ' '.join(usergroup)
		return [username,role_name,usergroup_name]

def perm_nav(request):
        '''根据放入session的uid查询出用户的菜单权限'''
        uid = request.session['user_id']
        u_obj = User.objects.get(id=uid)
        submenus_list = u_obj.perm.all()
        perm_dict = {}
        for submenu_list in submenus_list:
		if perm_dict.has_key(submenu_list.parent_menu.name):
			perm_dict[submenu_list.parent_menu.name].append(submenu_list)
		else:
			perm_dict[submenu_list.parent_menu.name] = [submenu_list]
        return perm_dict

def randomMAC():
	'''随机生成KVM MAC'''
	mac = [ 0x52, 0x54, 0x00,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" %x,mac))

def listkey():
        '''列出自动补齐key'''
        keys = SALTAPI.list_all_key()['return'][0]['data']['return']['minions']
        keylist = [key.encode() for key in keys]
        return keylist
