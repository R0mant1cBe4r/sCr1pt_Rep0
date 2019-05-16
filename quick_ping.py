# coding=utf-8

import datetime
import os


#ping判断是否连通
def get_ping_result(ip):
    #p = os.popen("ping -c 1 -w 1 "+ip)		#linux		发送单次ping请求
    p = os.popen("ping -n 1 -w 1 "+ip) 	#windows
    x = p.read()
    p.close()
    if x.count('TTL'):
    #if x.count('ttl'):
        return "OK"
    else:
        return "ERROR"

#从txt中获取ip地址
def txt_to_hosts(path):
    ip_list = []
    f = open(path,'r')
    line = f.readline()
    while line:
        l = str(line).strip()
        ip_list.append(l)
        line = f.readline()
    f.close()
    return ip_list


if __name__== "__main__":

    starttime = datetime.datetime.now()


    ip_list = txt_to_hosts("example.txt")

    f1 = open("example_result.txt","w")
    f2 = open("ip.txt","w")

    for i in ip_list:
        result = get_ping_result(i)
        print str(i)+": "+result
        f1.write(str(i)+": "+result+"\n")
        f1.flush()
        if result == "OK":
            f2.write(str(i)+"\n")
            f2.flush()

    f1.close()
    f2.close()

    endtime = datetime.datetime.now()
    print 'time: '+ str((endtime-starttime).seconds) + 's'
