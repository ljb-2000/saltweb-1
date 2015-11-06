from django.db import models

class Cobbler_Log(models.Model):
	hostname = models.CharField(max_length=200)
        interface = models.CharField(max_length=50)
        ip = models.IPAddressField()
        gateway = models.IPAddressField()
        dns = models.IPAddressField()
        mac = models.CharField(max_length=100)
        profile = models.CharField(max_length=500)
	user = models.CharField(max_length=100)
	date_joined = models.DateTimeField(null=True)
