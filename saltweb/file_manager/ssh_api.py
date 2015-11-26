#!/usr/bin/python

import paramiko,os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))

Local_Dir = os.path.join(BASE_DIR,'upload')

saltstack_ip = config.get('file_manager','saltstack_ip')
saltstack_username = config.get('file_manager','username')
saltstack_password = config.get('file_manager','password')
saltstack_remote_dir = config.get('file_manager','remote_dir')

class SSH(object):
	def __init__(self,ip,port,username,password):
		self.ip = ip
		self.port = port
		self.username = username
		self.password = password
		try:
			'''SFTP'''
			self.t = paramiko.Transport(self.ip,self.port)
			self.t.connect(username=self.username,password=self.password)
			self.sftp = paramiko.SFTPClient.from_transport(self.t)
			'''SSH'''
			self.ssh = paramiko.SSHClient()
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(self.ip,self.port,self.username,self.password)
		except Exception as e:
			return ""

	def exec_command(self,command):
		try:
			stdin,stdout,stderr = self.ssh.exec_command(command)
			return stdout.read()
		except Exception as e:
			return e
		else:
			self.ssh.close()
		
	def exec_command_list(self,command):
		'''return list'''
		try:
                	stdin,stdout,stderr = self.ssh.exec_command(command)
                	return stdout.readlines()
                except Exception as e:
                        return e
                else:
                        self.ssh.close()

	def send_file(self,local,remote):
		try:
			self.sftp.put(local,remote)
			return "send %s to %s success!" %(local,remote)
		except Exception as e:
			return "send %s to %s failed,%s" %(local,remote,e)
		else:
			self.t.close()

s=SSH(saltstack_ip,22,saltstack_username,saltstack_password)
