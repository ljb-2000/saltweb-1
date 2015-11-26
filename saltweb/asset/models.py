from django.db import models


class Host(models.Model):
	saltkey = models.CharField(max_length=200)
	hostname = models.CharField(max_length=100)
	ip = models.IPAddressField(unique=True)
	kernel = models.CharField(max_length=100)
	os = models.CharField(max_length=100)
	cpunum = models.CharField(max_length=50)
	cputype = models.CharField(max_length=100)
	memory = models.CharField(max_length=100)
	disk = models.CharField(max_length=100)
	comment = models.TextField(max_length=500,blank=True)

	def __str__(self):
		return '%s -- %s' %(self.hostname,self.ip)


class Network(models.Model):
	ip = models.IPAddressField(unique=True)
	device = models.CharField(max_length=200)
	comment = models.TextField(max_length=500,blank=True)

	def __str__(self):
		return "%s -- %s" %(self.device,self.ip)

class Storage(models.Model):
        ip = models.IPAddressField(unique=True)
        device = models.CharField(max_length=200)
        comment = models.TextField(max_length=500,blank=True)

        def __str__(self):
                return "%s -- %s" %(self.device,self.ip)
