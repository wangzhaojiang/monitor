from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import re
from monitor.function import function 


# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def state_cpu(request):
    result = function.cpu()
    return HttpResponse(result)

def state_port(request):
    result = function.netstat()
    return HttpResponse(result)

def state(request):
    return render_to_response('web/index.html')

def state_netstat(request):
    return render_to_response('web/network/status.html')
