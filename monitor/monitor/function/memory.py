#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-16 15:28
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import re



def getdata_memory():
    f = open('/proc/meminfo', 'r')
    content = f.readlines()
        
    option = ['^MemTotal:', '^MemFree:', '^Buffers:', '^Cached:', '^SwapTotal:', '^SwapFree:']

    data = {}

    for each_line in content:
        for search in option:
            result = re.findall(search, each_line)
            
            if len(result) != 0:
                option.remove(search)
                result = each_line.split()
                data[result[0]] = int(result[1])
                break

    f.close()

    return data


def memory():
    """内存使用率(MEMUsedPerc)=100*(MemTotal-MemFree-Buffers-Cached)/MemTotal"""
    
    data = getdata_memory()

    MEMusePerc = (data['MemTotal:'] - data['MemFree:'] - data['Buffers:'] - data['Cached:']) * 1.0 / data['MemTotal:']

    print '{\"Memtotal\": %s, \"MemUse\": %s, \"SwapTotal\": %s, \"SwapFree\": %s}' % (MEMusePerc, data['MemTotal:'], data['SwapTotal:'], data['SwapFree:'])

memory()
