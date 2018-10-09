#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
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
        res = requests.get('http://' + ur, headers=headers, verify=False)
        status = str(res.status_code)
        #print res.read()
    except Exception as e:
        res = requests.get('https://' + ur, headers=headers, verify=False)
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
        urlwrite(dic_code+"xx.txt", ur)
    except Exception as e:
        print ("* : "+ur + "   unreachable")
        urlwrite("unreachable.txt", ur)

#批量判断写入
def main(path):
    url = []
    url = urlread(path)
    for ur in url:
        selecode(ur)

if __name__ == '__main__':
    dnsinit()
    #print ("Now the script begins:")
    print ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    e1 = datetime.datetime.now()
    main("example.txt")
    e2 = datetime.datetime.now()
    print("* Spend time:"+str(e2-e1))
    print ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
