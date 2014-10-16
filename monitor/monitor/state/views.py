from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import re
from monitor.function import function 


# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def get_cpu(request):
    result = function.cpu()
    return HttpResponse(result)

def get_port(request):
    result = function.netstat()
    return HttpResponse(result)

def get_memory(request):
    result = function.memory()
    return HttpResponse(result)

def state(request):     #index
    return render_to_response('web/index.html')

def state_netstat(request):
    return render_to_response('web/network/status.html')

#def state_memory(request):
#    return render_to_response('')
#
def state_cpu(request):
    return render_to_response('web/cpu/cpu.html')
    
