from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import re

# Create your views here.

def hello(request):
    return render_to_response('hello.html')

def info(request):
    Basic = Basicinfo()
    content = []
    content.append(Basic._issue())
    content.append(Basic._uname())
    print Basic._ifconfig()
    return render_to_response('info.html', {'content': content, 'w': Basic._w(), 'netstat': Basic._netstat(),})
    
class Basicinfo():
    """the basic infomation of the computer"""
    def __init__(self):
        pass
    
    def _issue(self):
        issue = open('/etc/issue', 'r')
        content = issue.readlines()
        return ''.join(content) 

    def _uname(self):
        uname = os.popen('uname -a').readlines()
        return ''.join(uname)

    def _w(self):
        w = os.popen('w').readlines()
        return w

    def _netstat(self):
        netstat = os.popen('netstat -tunlp').readlines()
        return netstat

    def _ifconfig(self):
        ifconfig = os.popen('ifconfig').readlines()
        interface = []
        for tip in ifconfig:
            al = re.findall('^[^ ]\w+', tip)
            if al :
                interface.append(al)
        
