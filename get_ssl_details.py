# -*- coding: utf-8 -*-

#__Author__: Be4r

import ssl
import socket
import json
import datetime
import xlsxwriter
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#配置socket超时时间
timeout = 5   
socket.setdefaulttimeout(timeout)

#创建一个excel
workbook = xlsxwriter.Workbook('dns.xlsx')
#创建一个sheet
worksheet = workbook.add_worksheet('dns')

#写入字段名
def write_to_param(rowNum):
    headings = ['域名','通配符','证书品牌','过期时间','备注']
    worksheet.write_row('A'+str(rowNum), headings)

#写入证书细节
def write_cert_detail(rowNum, cert):
    worksheet.write_row('A'+str(rowNum),cert)

#获取证书细节
def get_cert_details(hostname):
	cert_detail = []
	try:
		ctx = ssl.create_default_context()
		s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
		s.connect((hostname, 443))
		cert = s.getpeercert()
		cert_detail.append(str(hostname))
		cert_detail.append(dict(x[0] for x in cert['subject'])['commonName'])
		cert_detail.append(dict(x[0] for x in cert['issuer'])['commonName'])	
		cert_detail.append(cert['notAfter'])
		cert_detail.append('')
	except:
		cert_detail.append(str(hostname))
		cert_detail.append('')
		cert_detail.append('')
		cert_detail.append('')
		cert_detail.append('')
	return cert_detail

#从txt中获取dns地址
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

#进度条展示
def get_progress_bar(id,num):
    percent = 1.0 * id / num * 100
    #print 'complete percent:' + str(percent) + '%', 
    print 'complete percent:%.2f' % percent + '%',   
    sys.stdout.write("\r")
    #time.sleep(0.1)   


if __name__ == '__main__':

    starttime = datetime.datetime.now()
    rowNum = 1
    write_to_param(rowNum)
    rowNum+=1
    dns = txt_to_hosts('result\\dns.txt')
    dnslenth = len(dns)
    print '* Sum: '+ str(dnslenth) + ''
    for key in dns:
    	cert_json = get_cert_details(key)
    	print '* ' + str(rowNum-1) + ': ' + str(cert_json)
    	write_cert_detail(rowNum,cert_json)
    	rowNum+=1
    	#get_progress_bar(rowNum-1,dnslenth)
		#print cert_json
		#print json.dumps(cert_json, encoding='utf-8', ensure_ascii=False)

	endtime = datetime.datetime.now()
    workbook.close()
    print ' * It takes time: '+ str((endtime-starttime).seconds) + 's'
