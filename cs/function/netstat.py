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
        
        #stat = "{\"type\": \"%s\", \"address\": \"%s\", \"pid_program_name\": \"%s\"}" % (each_line[0], each_line[3], each_line[5])
        stat = "%s, %s, %s" % (each_line[0], each_line[3], each_line[5])
        #print stat
        
        results.append(stat)
    
    #results ='[' + ','.join(results) + ']'
    
    #print results
    return results

def sql(result):
    time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
    
    conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'notamaiba',
            db = 'monitor'
            )
    
    cur = conn.cursor()

    for each_line in result:
        each_line = each_line.split()

        cur.execute(
                'insert into state_netstat(time, types, address, pid_programname) values(%s, %s, %s, %s)',
                (time_now, each_line[0], each_line[1], each_line[2])
                )
    
    cur.close()
    conn.commit()
    conn.close()

    sqldata = [time_now, each_line[0], each_line[1], each_line[2]]

    return sqldata



def main():
    result = netstat()
    sqldata = sql(result)
    return sqldata


if __name__ == '__main__':
    main()
