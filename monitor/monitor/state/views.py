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

def state_netstat(request):
    result = function.netstat()
    return HttpResponse(result)
