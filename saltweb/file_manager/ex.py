#!/usr/bin/pyhton
from ssh_api import *

s=SSH('192.168.38.10',22,'root','testing')

print s.send_file('/tmp/123','/tmp/123')
