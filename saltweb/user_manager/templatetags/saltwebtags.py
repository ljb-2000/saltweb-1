# coding: utf-8

from django import template
import json

register = template.Library()

@register.filter(name="format_time")
def format_time(date):
	return date.strftime('%Y-%m-%d %H:%M:%S')

@register.filter(name="format_json")
def format_json(string):
	return json.dumps(json.loads(string),sort_keys=True,indent=4)

@register.filter(name='count_user')
def count_user(groupobj):
	return groupobj.count()

@register.filter(name='bool2str')
def bool2str(value):
	if value:
		return u'是'
	else:
		return u'否'

@register.filter(name='group_str')
def group_str(group_list):
	return ' '.join([ group.name for group in group_list])

@register.filter(name='role_str')
def role_str(value):
	if value == 'SU':
		return u'超级用户'
	else:
		return u'普通用户'
