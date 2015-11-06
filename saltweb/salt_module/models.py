from django.db import models


class Module(models.Model):
        module_name = models.CharField(max_length=100,unique=True)
        module_info = models.TextField(max_length=500)
        args_info = models.TextField(max_length=500)
