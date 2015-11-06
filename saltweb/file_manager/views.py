#coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import os,json

def file_upload(request):
	return render_to_response('file_manager/file_upload.html',locals())

def uploadify_script(request):  
    ret="0"  
    file = request.FILES.get("Filedata",None)  
    if file:  
        result,new_name=profile_upload(file)  
        if result:  
            ret="1"  
        else:  
            ret="2"                      
    result = {'ret':ret,'save_name':new_name}  
    return HttpResponse(json.dumps(result))  
  
  
def profile_upload(file):  
    '''''文件上传函数'''  
    if file:  
        path=os.path.join('/home/huangchao','upload')  
        #file_name=str(uuid.uuid1())+".jpg"  
        file_name=str(uuid.uuid1())+'-'+file.name  
        #fname = os.path.join(settings.MEDIA_ROOT,filename)  
        path_file=os.path.join(path,file_name)  
        fp = open(path_file, 'wb')  
        for content in file.chunks():   
            fp.write(content)  
        fp.close()  
        return (True,file_name) #change  
    return (False,file_name)   #change 
