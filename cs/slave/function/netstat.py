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
import sys

#os.chdir(os.path.dirname('./' + sys.argv[0]))

#sys.path.append('../..')

from get_conf import *



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

    sqldata = []

    for each_line in result:
        each_line = each_line.split()

        cur.execute(
                'insert into state_netstat(ip, time, types, address, pid_programname) values(%s, %s, %s, %s, %s)',
                ('127.0.0.1', time_now, each_line[0], each_line[1], each_line[2])
                )
        sqldata.append([time_now, each_line[0], each_line[1], each_line[2]])
    
    cur.close()
    conn.commit()
    conn.close()


    return sqldata



def main():
    result = netstat()
    sqldata = sql(result)
    return sqldata


if __name__ == '__main__':
    main()
