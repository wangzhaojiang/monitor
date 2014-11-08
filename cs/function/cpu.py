#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-14 21:00
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

import time 
import MySQLdb



def getdata():
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
    """
    user_pass = user2 - user1
    system_pass = system2 - system1
    idle_pass = idle2 - idle1
    cpu利用率=(user_pass + system_pass)*100%/(user_pass + system_pass + idle_pass)
    """
    
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

    #result = "{\"user\": \"%s\", \"system\": \"%s\", \"all_use\": \"%s\"}" % (u_cpu_use, k_cpu_use, a_cpu_use) 
    result = [u_cpu_use, k_cpu_use, a_cpu_use] 

    return result
    
def sql(result):
    time_now = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
    
    conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'notamaiba',
            db = 'monitor',
            )
    cur = conn.cursor()

    cur.execute(
            'insert into state_cpu(time, user_use, system_use, all_use) values(%s, %s, %s, %s)',
            (time_now, result[0], result[1], result[2])
            )

    cur.close()
    conn.commit()
    conn.close()

    sqldata = [time_now, result[0], result[1], result[2]]
    
    return sqldata


def main():
    data_old = getdata()
    time.sleep(2)
    data_new = getdata()
    result = calculate(data_old, data_new)
    sqldata = sql(result)
    return sqldata


if __name__ == "__main__":
    main()
