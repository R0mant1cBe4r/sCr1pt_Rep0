# coding=utf-8

import nmap
import json
import datetime
import xlsxwriter
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#创建一个excel
workbook = xlsxwriter.Workbook(u"端口开放.xlsx")
#创建一个sheet
worksheet = workbook.add_worksheet("端口开放")


'''
#自定义样式，加粗
bold = workbook.add_format({'bold': 1})

#写入表头
headings = ['ip','漏洞名称','漏洞等级','漏洞类型','漏洞地址','漏洞细节','修复建议']
worksheet.write_row('A1', headings, bold)
'''

#写入字段名
def write_to_param(row_num):
    headings = ['PORT','STATE','SERVICE','VERSION']
    worksheet.write_row('A'+str(row_num), headings)

#写入port细节
def write_port_detail(row_num, port_select):
    worksheet.write_row('A'+str(row_num),port_select)

#创建nmap扫描
def scan(path):
    nm = nmap.PortScanner()
    #nmap_dict = nm.scan(hosts=ip, arguments='-T4 -A -v -p 1-65535 -O')
    nmap_dict = nm.scan(arguments='-T4 -A -v -p 1-65535 -O -iL '+path)
    #scan_result = nm[ip]
    #print nm.command_line()
    #print scan_result
    return nmap_dict

#获取port细节
def get_port_detail(port, ip_port_dict):
    port_detail_list = []
    port_detail_list.append(str(port)+"/tcp")
    port_detail_list.append(ip_port_dict[port]['state'])
    port_detail_list.append(ip_port_dict[port]['name'])
    if ip_port_dict[port]['product'] == "" and ip_port_dict[port]['version'] =="" and ip_port_dict[port]['extrainfo'] == "":
        port_detail_list.append(" ")
    elif ip_port_dict[port]['product'] == "" and ip_port_dict[port]['version'] =="" and ip_port_dict[port]['extrainfo'].strip():
        port_detail_list.append("("+ip_port_dict[port]['extrainfo']+")")
    elif ip_port_dict[port]['product'].strip() and ip_port_dict[port]['version'] =="" and ip_port_dict[port]['extrainfo'] == "":
        port_detail_list.append(ip_port_dict[port]['product'])
    elif ip_port_dict[port]['product'].strip() and ip_port_dict[port]['version'].strip() and ip_port_dict[port]['extrainfo'] == "":
        port_detail_list.append(ip_port_dict[port]['product']+" "+ip_port_dict[port]['version'])
    elif ip_port_dict[port]['product'] == "" and ip_port_dict[port]['version'].strip() and ip_port_dict[port]['extrainfo'].strip():
        port_detail_list.append(ip_port_dict[port]['version']+" ("+ip_port_dict[port]['extrainfo']+")")
    else:
        port_detail_list.append(ip_port_dict[port]['product']+" "+ip_port_dict[port]['version']+" ("+ip_port_dict[port]['extrainfo']+")")

    return port_detail_list

#进度条展示
def get_progress_bar(id,num):
    percent = 1.0 * id / num * 100
    #print 'complete percent:' + str(percent) + '%', 
    print 'complete   percent:%.2f' % percent + '%',   
    sys.stdout.write("\r")
    time.sleep(0.1)
    
if __name__== "__main__":
    
    starttime = datetime.datetime.now()

    print u"开始批量端口服务扫描"
    ip_port_dict = scan("example.txt")['scan']
    print u"端口服务扫描结束，开始整理数据"

    ip_lenth = len(ip_port_dict)
    progress = 1
    row_num = 1

    for ip in ip_port_dict:
        ip_row = [ip,'','','']
        worksheet.write_row('A'+str(row_num),ip_row)
        row_num = row_num+1
        write_to_param(row_num)
        row_num = row_num+1
        #print nmap_dict

        #port升序
        ip_port_sort = sorted(ip_port_dict[ip]['tcp'])

        #遍历获取all ports数据
        for port in ip_port_sort:
            port_detail_list = get_port_detail(port,ip_port_dict[ip]['tcp'])
            write_port_detail(row_num, port_detail_list)
            #print port_detail_list
            row_num = row_num+1
        
        ip_row[:] = []        
        get_progress_bar(progress,ip_lenth)
        progress = progress+1


    endtime = datetime.datetime.now()
    workbook.close()
    print 'time: '+ str((endtime-starttime).seconds) + 's'
