#!/usr/bin/python

from api import *

print SALTAPI.salt_mod('v6_pro_stage001','virt.vm_state')
