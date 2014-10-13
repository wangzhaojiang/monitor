from django.shortcuts import render_to_response
from django.http import HttpResponse
import os

# Create your views here.

def hello(request):
    return render_to_response('hello.html')

def info(request):
    etc_issue = open('/etc/issue','r')
    issue = etc_issue.readlines()
    issue = ' '.join(issue)
    content = []
    content.append(issue)
    etc_issue.close()
    uname = os.popen('uname -a').readlines()
    uname = ' '.join(uname)
    content.append(uname)
    return render_to_response('info.html', {'content': content})
    
