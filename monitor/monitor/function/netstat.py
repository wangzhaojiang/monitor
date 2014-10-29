#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-14 21:03
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import re
import os
import time
import MySQLdb


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
    
    print results
    return results

def sql(result):
    time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    
    conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'notamaiba',
            db = 'monitor'
            )
    
    cur = conn.cursor()

    cur.execute(
            'insert into state_netstat(time)'
            )



if __name__ == '__main__':
    result = netstat()
    sql(result)
