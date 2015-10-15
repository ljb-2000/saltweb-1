from django.db import models

class Host(models.Model):
        saltkey = models.CharField(max_length=200)
        hostname = models.CharField(max_length=100)
        ip = models.IPAddressField(unique=True)
        comment = models.TextField(max_length=500,blank=True)

        def __str__(self):
                return '%s -- %s' %(self.hostname,self.ip)
