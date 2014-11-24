#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-15 19:26
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import time 
import re
import os


def netstat():
    content = os.popen('netstat -tunlp').readlines()
    
    del content[1]
    del content[0]
    
    results = []
    
    for each_line in content:
        each_line = each_line.split()
        if 'LISTEN' in each_line:
            each_line.remove('LISTEN')
        
        stat = "{\"type\": \"%s\", \"address\": \"%s\", \"pid_program_name\": \"%s\"}" % (each_line[0], each_line[3], each_line[5])
        
        results.append(stat)
    
    results ='[' + ','.join(results) + ']'
    
    
    return results


def getdata_cpu():
    f = open('/proc/stat', 'r')    
    
    stat = f.readlines()
    
    cpu = stat[0]
    cpu = cpu.split()
    cpu = cpu[1:8]

    num = 0

    while num < 7:
        cpu[num] = int(cpu[num])
        num = num + 1

    f.close()

    return cpu

def calculate(data_old, data_new):
    
    def addall(data):
        result = 0

        for ele in data:
            result = result + ele
        
        return result

    co_time = addall(data_old)
    cn_time = addall(data_new)

    user_pass = data_new[0] - data_old[0]
    system_pass = data_new[2] - data_old[2]
    cpu_pass = cn_time - co_time

    u_cpu_use = user_pass * 1.0 / cpu_pass
    k_cpu_use = system_pass * 1.0 / cpu_pass
    a_cpu_use = u_cpu_use + k_cpu_use

    result = "{\"user\": \"%s\", \"system\": \"%s\", \"all_use\": \"%s\"}" % (u_cpu_use, k_cpu_use, a_cpu_use) 

    return result
    

def cpu():
    data_old = getdata_cpu()
    time.sleep(1)
    data_new = getdata_cpu()
    result = calculate(data_old, data_new)
    
    return result

def getdata_memory():
    f = open('/proc/meminfo', 'r')
    
    data = []
    num = 0 # 只读取前四行

    while num < 4:
        content = f.readline()
        content = content.split()

        content[1] = int(content[1])
        
        data.append(content[1])

        num += 1


    return data


def memory():
    """内存使用率(MEMUsedPerc)=100*(MemTotal-MemFree-Buffers-Cached)/MemTotal"""
    data = getdata_memory()

    MEMusePerc = (data[0] - data[1] - data[2] - data[3]) * 1.0 / data[0]

    return '{\"MemUse\": %s}' % MEMusePerc
