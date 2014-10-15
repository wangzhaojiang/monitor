from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import re

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

#def info(request):
#    return render_to_response('info.html', {'content': content, 'w': Basic._w(), 'netstat': Basic._netstat(),})
#    
#class Basicinfo():
#    """the basic infomation of the computer"""
#    def __init__(self)
#        pass
#    
#    def _issue(self):
#        issue = open('/etc/issue', 'r')
#        content = issue.readlines()
#        return ''.join(content) 
#
#    def _uname(self):
#        uname = os.popen('uname -a').readlines()
#        return ''.join(uname)
#
#    def _w(self):
#        w = os.popen('w').readlines()
#        return w
#
#    def _netstat(self):
#        netstat = os.popen('netstat -tunlp').readlines()
#        return netstat
#
#    def _ifconfig(self):
#        ifconfig = os.popen('ifconfig').readlines()
#        interface = []
#        for tip in ifconfig:
#            tmp = re.findall('^[^ ]\w+', tip)
#            if tmp :
#                interface.append(tmp)
#        ip = []
#        for tip in interface:
#            tmp1 = tip[0]
#            tmp2 = os.popen('ifconfig ' + tmp1).readlines()
#            for tmp3 in tmp2:
#                tmp4 = re.findall('inet ', tmp3)
#                if tmp4:
#                    tmp3 = tmp3.split()
#                    print tmp1,
#                    print tmp3[1],
#                    print tmp3[3]
#
#
