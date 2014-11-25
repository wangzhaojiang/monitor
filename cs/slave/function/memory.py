#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-16 15:28
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import re
import MySQLdb
import time
import os
import sys

#os.chdir(os.path.dirname('./' + sys.argv[0]))

#sys.path.append('../../')

from get_conf import *




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

    Memuse = (data['MemTotal:'] - data['MemFree:'] - data['Buffers:'] - data['Cached:']) * 1.0 / data['MemTotal:']

    #print '{\"MemUse\": %s, \"MemTotal\": %s, \"SwapTotal\": %s, \"SwapFree\": %s}' % (MEMusePerc, data['MemTotal:'], data['SwapTotal:'], data['SwapFree:'])
    
    return [data, Memuse]


def sql(result):
    data = result[0]
    Memuse = result[1]

    time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
    #os.chdir(os.path.dirname('../../'))
    param = get_conf_data()

    conn = MySQLdb.connect(
            host = param['database_host'],
            port = int(param['database_port']),
            user = param['database_user'],
            passwd = param['database_passwd'],
            db = param['database_db'],
            )
    cur = conn.cursor()

    cur.execute(
            'insert into state_memory(ip, time, memuse, memtotal, swaptotal, swapfree) values(%s, %s, %s, %s, %s, %s)',
            ('127.0.0.1', time_now, Memuse, data['MemTotal:'], data['SwapTotal:'], data['SwapFree:']))

    cur.close()
    conn.commit()
    conn.close()

    sqldata = [time_now, Memuse, data['MemTotal:'], data['SwapTotal:'], data['SwapFree:']]

    return sqldata



def main():
    result = memory()
    sqldata = sql(result)
    return sqldata


if __name__ == '__main__':
    main()
