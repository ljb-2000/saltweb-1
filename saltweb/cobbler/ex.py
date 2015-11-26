#!/usr/bin/python

from cobbler_api import *

print u_cobbler_api.add_system('ttt','192.168.1.10','eth0','192.168.1.1','11:ff:12:aa:ff:ac','8.8.8.8','xinxindai_CentOS6.4-x86_64_Base')
