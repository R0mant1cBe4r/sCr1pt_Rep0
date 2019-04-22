# -*- coding: utf-8 -*- 
# /usr/bin/env python3

#转自https://www.freebuf.com/sectool/199622.html

import os
import argparse

class Interval(object):
    def __init__(self):
        self.st=bin(0)
        self.ed=bin(0)
    def change(self,new_st,new_ed):
        self.st=new_st
        self.ed=new_ed

def file_read(oldpath):
    oldfile=open(oldpath,'r')
    print('\033[1;34m'+'[-]Reading file...'+'\033[0m')
    IP_line="".join(oldfile.readlines())
    oldfile.close()
    count=0
    for i in enumerate(open(oldpath,'r')):
        count+=1
    return IP_line.splitlines(),count

def file_write(newpath,intervals):
    newfile=open(newpath,'w')
    write_IP=merge(intervals)
    print('\033[1;34m'+'[-]Writing in file...'+'\033[0m')
    for interval in write_IP:
        if interval.st!=interval.ed:
            newfile.write(LongToIP(interval.st)+'-'+LongToIP(interval.ed)+'\n')
        else:
            newfile.write(LongToIP(interval.st)+'\n')
    return len(write_IP)
def IPToLong(strIP):
    try:
        ip=[]
        single=strIP.split('.')
        for single_ip in single:
            ip.append(int(single_ip))
        return bin((ip[0]<<24)+(ip[1]<<16)+(ip[2]<<8)+ip[3])
    except Exception as e:
        return bin(0)

def LongToIP(longIP):
    IP_list=[]
    IP_list.append(str(eval(longIP) >>24))
    IP_list.append(str((eval(longIP) & 0xffffff)>>16))
    IP_list.append(str((eval(longIP) & 0xffff)>>8))
    IP_list.append(str((eval(longIP) & 0xff)))
    return '.'.join(IP_list)

def merge(intervals):
    interval_tmp=Interval()
    res=[interval_tmp]
    if len(intervals)==0:return res
    intervals.sort(key=lambda intervals_sort: int(intervals_sort.st,base=2))
    res[0]=intervals[0]
    for i in range(1,len(intervals)):
        if int(intervals[i].st,base=2)<=int(res[len(res)-1].ed,base=2):
            max_ed=max(int(intervals[i].ed,base=2),int(res[len(res)-1].ed,base=2))
            res[len(res)-1].ed=bin(max_ed)
        else:
            res.append(intervals[i])
    return res

def main(oldpath):
    IP_list,before_merge=file_read(oldpath)
    IP_interval=[]
    IP_tmp=[IPToLong('0.0.0.0'),IPToLong('0.0.0.0')]
    for IP_range in IP_list:
        if '-' in IP_range:
            interval_tmp=Interval()
            tmp=IP_range.split('-')
            if len(tmp)==2:
                IP_tmp[0]=(IPToLong(tmp[0]))
                IP_tmp[1]=(IPToLong(tmp[1]))
                interval_tmp.change(IP_tmp[0],IP_tmp[1])
                IP_interval.append(interval_tmp)
        elif '/' in IP_range:
            interval_tmp=Interval()
            tmp=IP_range.split('/')
            if len(tmp)==2:
                ip1=tmp[0]
                ip2=tmp[1]
                ip1_tmp=ip1.split('.')
                if ip1[-1]=='0':
                    ip1=ip1[:-1]+'1'
                for i in range(len(ip1_tmp)):
                    ip1_tmp[i]=bin(int(ip1_tmp[i]))[2:].rjust(8)
                    ip1_tmp[i]=ip1_tmp[i].replace(' ','0')
                ip1_tmp=''.join(ip1_tmp)
                ip2_tmp=ip1_tmp[0:int(ip2)].ljust(32)
                ip2_tmp=ip2_tmp.replace(' ','1')
                ip1_tmp=[]
                for j in range(0,31,8):
                    ip1_tmp.append(str(int(ip2_tmp[j:j+8],base=2)))
                ip2='.'.join(ip1_tmp)
                interval_tmp.change(IPToLong(ip1),IPToLong(ip2))
                IP_interval.append(interval_tmp)
        else:
            interval_tmp=Interval()
            interval_tmp.change(IPToLong(IP_range),IPToLong(IP_range))
            IP_interval.append(interval_tmp)
    newpath=os.path.join(os.path.split(oldpath)[0],'new_'+os.path.split( oldpath)[1])
    after_merge=file_write(newpath,IP_interval)
    print('\033[1;31m'+'[+]Complete!\nBefore the merger:'+str(before_merge)+' After the merger:'+str(after_merge)+'\033[0m')
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-p',help='Old IP_Inteval File Path')
    args=parser.parse_args()
    if args.p:
        main(args.p)
    else:
        print('\033[1;31m'+'[-]Please enter the correct parameters'+'\033[0m')
