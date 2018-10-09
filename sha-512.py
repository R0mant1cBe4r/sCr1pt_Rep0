#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import string
import hashlib
import datetime

#文件读取
def pwdread(path):
    pwd = []
    f = open(path, 'r')
    line = f.readline()
    while line :
        l = str(line).strip()
        pwd.append(l)
        line = f.readline()
    f.close()
    return pwd

#文件写入
def pwdwrite(path_, pwd):
    f_ = open(path_, 'a+')  #执行文件之前先将旧文件删除
    f_.write(pwd+"\n")
    f_.flush()
    f_.close()

#sha512
def sha_512(pwd):
    salt = "hV2VRhZO"
    pwd_hash = hashlib.sha512()
    pwd_hash.update(salt+pwd)
    return pwd_hash.hexdigest()

def main(path, path_):
    passwd = []
    passwd = pwdread(path)
    for pwd in passwd:
        pwdwrite(path_, sha_512(pwd))   

if __name__ == '__main__':
    e1 = datetime.datetime.now()
    main("pwd.txt", "sha512_pwd.txt")
    e2 = datetime.datetime.now()
    print("Spend time:"+str(e2-e1))


