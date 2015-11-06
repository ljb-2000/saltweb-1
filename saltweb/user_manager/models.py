from django.db import models

class UserGroup(models.Model):
        name = models.CharField(max_length=80,unique=True)
        comment = models.CharField(max_length=160,blank=True)

        def __unicode__(self):
                return self.name

class User(models.Model):
        '''SU =1 , CU = 0'''
        USER_ROLE_CHOICES = (
                ('SU' , 'SuperUser'),
                ('CU' , 'CommonUser'),
        )
        username = models.CharField(max_length=80,unique=True)
        password = models.CharField(max_length=100)
        email = models.EmailField(max_length=75)
        role = models.CharField(max_length=2,choices=USER_ROLE_CHOICES,default='CU')
        group = models.ManyToManyField(UserGroup)
        is_active = models.BooleanField(default=True)
        last_login = models.DateTimeField(null=True)
        date_joined = models.DateTimeField(null=True)

        def __unicode__(self):
                return self.username
