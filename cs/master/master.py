#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-01 17:39
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import socket
import threading
import MySQLdb
import sys
import os
#切换工作目录， 为了下面的'''import'''
os.chdir(os.path.dirname('./' + sys.argv[0]))

sys.path.append('..')

from get_conf import *

BUFSIZ = 4096

def server_socket():

    os.chdir(os.path.dirname('../'))
    data = get_conf_data()

    HOST = ''
    PORT = int(data['trans_port'])
    ADDR = (HOST, PORT)

    sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sersock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sersock.bind(ADDR)
    sersock.listen(5)

    while True:
        #print 'Waiting for the connection ...'
        clisock, addr = sersock.accept()
        print 'connection from :', addr
    
        
        try:
            thread = process(clisock)
            thread.start()
            clisock.close()
        
        except:
            print 'ERROR'
    

class process(threading.Thread):
    def __init__(self, clisock):
        
        global BUFSIZ

        self.clisock = clisock
        self.data = self.clisock.recv(BUFSIZ).split('^^')
        self.categoty = ['cpu', 'diskio', 'flow', 'memory', 'netstat']

        threading.Thread.__init__(self)
        

    def run(self):
        'PROCESSING ...'
        self.host = self.data[0]
        del self.data[0]
        self.ip = self.data[0]
        del self.data[0]

        #print self.data

        self.result = {}

        while True:
            off = self.data.index('|')
            tmp = self.data[0:off]
            self.result[tmp[0]] = tmp[1:off]

            #delete the used data
            count = 0

            while count < (off + 1):
                del self.data[0]
                count += 1

            if len(self.data) <= 1:
                break

        self.sql_data()

    def sql_data(self):
        data = get_conf_data()
        conn = MySQLdb.connect(
                host = data['database_host'], 
                user = data['database_user'], 
                passwd = data['database_passwd'], 
                port = int(data['database_port']))

        cur = conn.cursor()
        conn.select_db(data['database_db'])

        #sql cpu_data
        cpu_data = self.result['cpu']
        value = [self.ip, cpu_data[0], cpu_data[1], cpu_data[2], cpu_data[3]]
        
        cur.execute(
                'insert into state_cpu(ip, time, user_use, system_use, all_use) values(%s, %s, %s, %s, %s)',
                value)

        print 'cpu_data sql done'
        
        #sql memory_data
        memory_data = self.result['memory']
        value = [self.ip, memory_data[0], memory_data[1], memory_data[2], memory_data[3], memory_data[4]]

        cur.execute(
                'insert into state_memory(ip, time, memuse, memtotal, swaptotal, swapfree) values(%s, %s, %s, %s, %s, %s)',
                value)

        print 'memory_data sql done'

        #sql diskio_data
        diskio_data = self.result['diskio']
        value = [self.ip, diskio_data[0], diskio_data[1], diskio_data[2]]

        cur.execute(
                'insert into state_diskio(ip, time, pgpgin, pgpgout) values(%s, %s, %s, %s)',
                value)

        print 'diskio_data sql done'

        #sql flow_data
        flow_data = str(self.result['flow'])
        #上面的str 是为了下面能够用split() 函数进行分离

        #'''''''''''''stupid way to process the data'''''''''''''''

        #for each in flow_data:
        #    each = each.split(',')
        #    length = len(each[0].strip())
        #    time = each[0].strip()[2:(length - 1)]
        #    length = len(each[1].strip())
        #    interface = each[1].strip()[1:(length - 2)]
        #    byte = each[2].strip()
        #    length = len(each[3].strip())
        #    packets = each[3].strip()[0:(length - 1)]

        #    value = [self.ip, time, interface, byte, packets]
        #    
        #    cur.execute(
        #            'insert into state_flow(ip, time, interface, byte, packets) values(%s, %s, %s,%s, %s)',
        #            value
        #            )
        
        for each in flow_data.split(']'):
            each = each.strip('\' \" \,\[')
            
            value = [self.ip]

            if (each != ""):
                each = each.split(',')
                for tmp in each :
                    tmp = tmp.strip('\" \,')
                    if(tmp != ''):
                        value.append(tmp)

            #print value

            if(len(value) > 1):
                cur.execute(
                        'insert into state_flow(ip, time, interface, byte, packets) values(%s, %s, %s,%s, %s)',
                        value
                        )
        
        print 'flow_data sql done'

        #sql netstat_data
        netstat_data = str(self.result['netstat']) 
        #上面的str 是为了下面能够用split() 函数进行分离
        
        for each in netstat_data.split(']'):
            each = each.strip('", [')
            
            value = [self.ip]

            if(each != ""):
                each = each.split(',')
                #print each
                for tmp in each:
                    tmp = tmp.strip('\" \'')
                    if(tmp != ""):
                        value.append(tmp)
            
            #print value
            if (len(value) > 1):
                cur.execute(
                        'insert into state_netstat(ip, time, types, address, pid_programname) values(%s, %s, %s, %s, %s)',
                        value
                        )

        print 'netstat_data sql done'


        cur.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    server_socket()
