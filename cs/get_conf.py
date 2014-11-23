#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-23 23:27
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------

def get_conf_file(param):
    file = open(param, 'r')
    content = file.readlines()
    file.close()
    return content

# 过滤注释
def data_filter(content):
    data = []
    for each_line in content:
        each_line = each_line.strip()
        if (each_line != '' and each_line[0] != '#'):
            useful = each_line.split('=')
            data.append(useful)
    return data


class Myerror(Exception):
    def __init__(self, error_info):
        print error_info


def get_conf_data():
    data = {}

    #get the conf data
    content = get_conf_file('conf/monitor.conf')
    monitor_conf = data_filter(content)
    for each in monitor_conf:
        data[each[0]] = each[1]

    #get the master_node data
    content = get_conf_file('conf/master_node')
    master_node = data_filter(content)
    if(len(master_node) != 1):
        error_info = 'master 节点个数大于 1'
        raise Myerror(error_info)
    else:
        data['master_node'] = master_node[0][0]

        
    #get the slave_node data
    content = get_conf_file('conf/slave_node')
    tmp = data_filter(content)
    slave_node = []

    for each in tmp:
        slave_node.append(each[0])

    data['slave_node'] = slave_node

    print data


    



if __name__ == '__main__':
    get_conf_data()
