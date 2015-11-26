from django.db import models

class LoginLog(models.Model):
	login_time = models.DateTimeField()
	username = models.CharField(max_length=100)
	ip = models.IPAddressField()
 	

class CommandLog(models.Model):
	exec_time = models.DateTimeField()
	username = models.CharField(max_length=100)
	exec_moudle = models.CharField(max_length=100)
	exec_args = models.CharField(max_length=200)
