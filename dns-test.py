#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
import threading
import datetime

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#init
def dnsinit():
    print '''      _                         _                  _   
   __| |  _ __    ___          | |_    ___   ___  | |_ 
  / _` | | '_ \  / __|  _____  | __|  / _ \ / __| | __|
 | (_| | | | | | \__ \ |_____| | |_  |  __/ \__ \ | |_ 
  \__,_| |_| |_| |___/          \__|  \___| |___/  \__|
                                                       '''

def dnsinit2():
    print "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * "


#文件读取
def urlread(path):
    url = []
    f = open(path, 'r')
    line = f.readline()
    while line :
        l = str(line).strip()
        url.append(l)
        line = f.readline()
    f.close()
    return url


#文件写入
def urlwrite(path_, ur):
    f_ = open(path_, 'a+')  #执行文件之前先将旧文件删除
    f_.write(ur+"\n")
    f_.flush()
    f_.close()


#获取httpcode
def urlcode(ur):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    try:
        res = requests.get('http://' + ur, headers=headers,verify=False, timeout=10)
        status = str(res.status_code)
        #print res.read()
    except Exception as e:
        res = requests.get('https://' + ur, headers=headers, verify=False, timeout=10)
        status = str(res.status_code)
        #print res.read()
    return status


#code字典
def dic(code):
    params = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5"
    }
    return params[code]


#判断code
def selecode(ur):
    try:
        url_code = urlcode(ur)
        dic_code = dic(url_code[0])
        print ("* : "+ur + "   status:" + url_code)
        urlwrite("output-file/"+dic_code+"xx.txt", ur)
    except Exception as e:
        #print e
        print ("* : "+ur + "   unreachable")
        urlwrite("output-file/unreachable.txt", ur)


url = []
url = urlread("dns-file/test1.txt")
threads = []
files = range(len(url))

for ur in url:
    t = threading.Thread(target=selecode, args=(ur, ))
    threads.append(t)


if __name__ == '__main__':
    dnsinit()
    dnsinit2()
    e1 = datetime.datetime.now()

    for i in files:
        #print threads[i].getName()
        threads[i].setDeamon=True
        threads[i].start()
    for i in files:
        threads[i].join()
        
    
    e2 = datetime.datetime.now()
    print("* Spend time:"+str(e2-e1))
    dnsinit2()
