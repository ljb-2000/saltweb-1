# coding: utf-8
from django.core.paginator import Paginator
import urllib,urllib2
import json
import os

SALT_URL="https://192.168.38.10:8000"
SALT_USERNAME='huangchao'
SALT_PASSWORD='huang7361623'

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
		format_arg = ''
		url = self.__url.rstrip('/')
		headers = {'X-Auth-Token' : self.__token, 'Accept' : 'application/json'}
		if args:
			for arg in args:
				format_arg += urllib.urlencode({'arg' : arg})+'&'	
			r_args = urllib.urlencode(params)+'&'+format_arg.rstrip('&')
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

	def set_file(self,key,source,dest):
		self.get_token()
		headers = {'X-Auth-Token' : self.__token, 'Accept' : 'application/json'}
		params = {'client' : 'local', 'tgt' : key, 'fun' : 'cp.get_url'}
		ret = self.postRequest(params,source,dest)
		return ret

	def lookup_jid(self,jid):
		self.get_token()
		params = {'client' : 'runner' , 'fun' : 'jobs.lookup_jid' , 'jid' : jid}
		ret = self.postRequest(params)
		return ret

	def cmd(self,key,command):
		self.get_token()
		params = {'client' : 'local' , 'tgt' : key, 'fun': 'cmd.run'}
		ret = self.postRequest(params,command)
		return ret

	def salt_mod(self,key,mod_name,*args):
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
