from django.http import HttpResponse
from django.shortcuts import render_to_response

def hosts(request):
        return HttpResponse('test')
