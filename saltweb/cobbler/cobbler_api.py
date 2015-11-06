#!/usr/bin/python

import ConfigParser,os
import xmlrpclib 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))

cobber_xmlrpc_url = config.get('cobbler','xmlrpc_url')
cobber_xmlrpc_username = config.get('cobbler','username')
cobber_xmlrpc_pwd = config.get('cobbler','password')

class CobblerAPI():
	def __init__(self,url,username,password):
		self.cobbler_url = url
		self.cobbler_username = username
		self.cobbler_password = password
		try:
			self.remote = xmlrpclib.Server(self.cobbler_url)
			self.token = self.remote.login(self.cobbler_username,self.cobbler_password)
			self.system_id = self.remote.new_system(self.token)
		except:
			pass
	
	def seach_profile(self):
		profile_list = self.remote.get_profiles()
		return [x.get('name') for x in profile_list]

        def seach_system(self):
                system_list = self.remote.get_systems()
		return [x.get('name') for x in system_list]


	def add_system(self,hostname,ip_add,interface,gateway,mac_add,dns_server,profile):
		try:
			self.remote.modify_system(self.system_id,"name",hostname,self.token)
			self.remote.modify_system(self.system_id,"hostname",hostname,self.token)
			self.remote.modify_system(self.system_id,"gateway",gateway,self.token)
			self.remote.modify_system(self.system_id,"name_servers",dns_server,self.token)
			self.remote.modify_system(self.system_id,"modify_interface",{
				"macaddress-"+interface: mac_add,
				"ipaddress-"+interface: ip_add,
				"subnet-"+interface:"255.255.255.0",
				"static-"+interface:"1",
			},self.token)
			self.remote.modify_system(self.system_id,"profile",profile,self.token)
			self.remote.save_system(self.system_id,self.token)
			self.remote.sync(self.token)
			return "success"
		except Exception as e:
			return 'host: %s add failed: %s' %(hostname,e)

	def del_system(self,system_name):
		try:
			self.remote.remove_system(system_name,self.token)
			self.remote.sync(self.token)
			return "success"
                except Exception as e:
                	return 'host: %s delete failed: %s' %(system_name,e)	

u_cobbler_api = CobblerAPI(cobber_xmlrpc_url,cobber_xmlrpc_username,cobber_xmlrpc_pwd)
