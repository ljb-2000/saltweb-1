#!/usr/bin/python

from api import *
print SALTAPI.salt_mod('test_v6_lvs01','cp.get_file',['salt://upload/logo.png','/tmp/logo.png'])
#print SALTAPI.salt_mod('test_v6_lvs01','cmd.run',['date'])
