#!/bin/python
# Upload data to SaltWeb
# Using the root user for it

import httplib
import urllib
import commands
import socket
import re


def Collect():
	'''collect information'''
        hostname = commands.getoutput("hostname")
        ip = socket.gethostbyname(socket.gethostname())
        kernel = commands.getoutput("uname -r")
        os = commands.getoutput('cat /etc/issue | sed -n "1"p')
        cpunum = commands.getoutput('cat /proc/cpuinfo  | grep "model name" | wc -l')
        cputype = commands.getoutput('cat /proc/cpuinfo  | grep "model name" | cut -f2 -d: | uniq')
        memory = commands.getoutput(' cat /proc/meminfo | grep MemTotal | cut -f2 -d:')
        disk_info = commands.getoutput('fdisk -l | grep "Disk /" | cut -f1 -d,')
        disk = re.search(r'Disk.*',disk_info).group(0)
	host_info = {
		"saltkey": hostname.strip(),
		"hostname": hostname.strip(),
		"ip": ip.strip(),
		"kernel": kernel.strip(),
		"os": os.strip(),
		"cpunum": cpunum.strip(),
		"cputype": cputype.strip(),
		"memory": memory.strip(),
		"disk": disk.strip()
	}
	return host_info



def UpLoad(host,method,url,args):
	data = urllib.urlencode(args)
	headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
	try:
		conn = httplib.HTTPConnection(host,80,timeout=10)
		conn.request(method,url,data,headers)
		httpres = conn.getresponse()
		print httpres.read()
	except httplib.HTTPException as e:
		print "request error: ",e



if __name__ == '__main__':
	args = Collect()
	host = "127.0.0.1"
	method = "POST"
	url = "/asset/add_host_service/"
	UpLoad(host,method,url,args)
