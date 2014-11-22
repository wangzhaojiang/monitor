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



HOST = ''
PORT = 10000
BUFSIZ = 4096
ADDR = (HOST, PORT)


def server_socket():

    global HOST
    global PORT
    global BUFSIZ
    global ADDR

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
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'notamaiba', port = 3306)
        cur = conn.cursor()
        conn.select_db('monitor')

        #sql cpu_data
        cpu_data = self.result['cpu']
        value = [self.ip, cpu_data[0], cpu_data[1], cpu_data[2], cpu_data[3]]
        
        cur.execute('insert into state_cpu(ip, time, user_use, system_use, all_use) values(%s, %s, %s, %s)', value)
        
        #sql memory_data
        memory_data = self.result['memory']
        value = [self.ip, memory_data[0], memory_data[1], memory_data[2], memory_data[3], memory_data[4]]

        cur.execute('insert into state_memory(ip, time, memuse, memtotal, swaptotal, swapfree) values(%s, %s, %s, %s, %s, %s)',value)

        #sql diskio_data
        diskio_data = self.result['diskio']
        value = [self.ip, diskio_data[0], diskio_data[1], diskio_data[2]]

        cur.execute('insert into state_diskio(ip, time, pgpgin, pgpgout) values(%s, %s, %s, %s)',value)





if __name__ == '__main__':
    server_socket()
