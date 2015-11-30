from django.db import models

class Parent_Menu(models.Model):
        name = models.CharField(max_length=200)

class Sub_Menu(models.Model):
        name = models.CharField(max_length=200)
	url = models.CharField(max_length=500)
	parent_menu = models.ForeignKey(Parent_Menu)
