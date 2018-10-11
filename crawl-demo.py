#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests

def getData(url, data=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'http://xxx.cn/',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://xxx.cn',
        'Cookie': 'sessionid=xxx'
    }
    return requests.post(url, data=data, headers=headers)

def getIPS(url):
    ips = list()
    for i in xrange(1, 122):
        params = {
            'limit': 10,
            'offset': i,
            'sortOrder': 'asc',
            # 'keyword': '1'
        }
        data = getData(url, params).json()
        for info in  data['data_set']:
            # print "主机名:{}  ip地址: {}".format(info['host_name'], info['ip'])
            if not info['ip'].startswith('10'):
                print info['ip']
            ips.append(info['ip'])
    
    return ips

if __name__ == "__main__":
    f = open("ip.txt", "w")
    url = 'http://xxx.cn/xxx'
    for ip in getIPS(url):
        print ip
        f.write(ip + "\n")
    f.close()
