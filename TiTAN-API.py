# -*- coding: utf-8 -*-

from __future__ import absolute_import
import httplib
import json
import time
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

host = "xx.xx.xxx.xxx"
port = 6000

#登录认证
def login():
	url = "http://%s:%s/v1/api/auth" % (host, port)
	header = {"Content-Type": "application/json"}
	body = {"username": "your username", "password": "your password"}
	json_body = json.dumps(body)
	conn = httplib.HTTPConnection(host,port)
	conn.request(method="POST", url=url, body=json_body, headers=header)
	#conn.request('POST', url, json_body, header)
	response = conn.getresponse()
	res = response.read()
	#print json.loads(res)
	return json.loads(res)

#发送请求
def send_request(method, url, data):
	login_result = login()
	sign_key = login_result.get("data").get("signKey")
	jwt = login_result.get("data").get("jwt")
	comid = login_result.get("data").get("comId")
	
	#时间戳
	ts = int(time.time())

	if data is not None:
		info = ""
		if method == "GET":
			#对参数key进行字典排序
			keys = sorted(data.keys())
			for key in keys:
				info  = info+key+str(data.get(key))
				#print info
		elif method == "POST" or method == "PUT" or method == "DELETE":
			info = json.dumps(data)

		#拼接待签名字符串
		to_sign = str(comid)+str(info)+str(ts)+str(sign_key)
	else:
		to_sign = str(comid)+str(ts)+str(sign_key)
	#print to_sign
	#对待签名字符串进行sha1得到签名字符串
	sign = hashlib.sha1(to_sign).hexdigest()

	#组装http请求头参数
	header = {"Content-Type": "application/json", "comId": comid, "timestamp": ts, "sign": sign, "Authorization": "Bearer "+jwt}
	conn = httplib.HTTPConnection(host, port)
	conn.request(method=method, url=url, body=json.dumps(data), headers=header)
	response = conn.getresponse()
	res = response.read()
	return json.loads(res)

#获取动态蜜罐所有数据信息
def get_honeypot():
	#url = "http://%s:%s/external/api/detect/honeypot/linux?page=0&size=5000000" % (host, port)
	iport = raw_input('Input your port, then Enter: ')
	#print len(iport)
	#print type(iport)
	print 'Start grabbing honeypot data...'
	url = "http://%s:%s/external/api/detect/honeypot/linux?page=0&size=200" % (host, port)
	data = {'page': 0, 'size': 200}
	res = send_request("GET", url, data)
	#print json.dumps(res, encoding='utf-8', ensure_ascii=False)
	print 'Data crawling is complete, start to organize data...'
	f = open('honeypot.txt','w+')
	f.write('发现时间'+'             '+'源IP'+'         '+'目标主机IP'+'     '+'端口'+' '+'业务组'+'\n')
	f.flush()
	for key in res['rows']:
		if str(key['port']) == iport:
			#print str(timestamp_to_time(key['time']))+'  '+key['clientIp']+'  '+key['connectionIp']+'  '+str(key['port'])+'  '+str(key['bizGroup'])
			f.write(str(timestamp_to_time(key['time']))+'  '+key['clientIp']+'  '+key['connectionIp']+'  '+str(key['port'])+'  '+str(key['bizGroup'])+'\n')
			f.flush()
	f.close()
	print 'Honeypot.txt Data finishing'


#时间戳转换
def timestamp_to_time(timestamp):
	timeArray = time.localtime(timestamp)
	otherStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray)
	return otherStyleTime

if __name__ == '__main__':

    get_honeypot()
