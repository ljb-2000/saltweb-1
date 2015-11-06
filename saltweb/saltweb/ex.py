#!/usr/bin/python

from api import *
print SALTAPI.salt_mod('test_v6_lvs0*','cp.get_file',['salt://a','/tmp/a'])
