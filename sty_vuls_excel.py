# coding=utf-8

import requests
import json
import hashlib
import xlsxwriter
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#f = open("test.txt", "w")

#创建一个excel
workbook = xlsxwriter.Workbook("vuls.xlsx")
#创建一个sheet
worksheet = workbook.add_worksheet("vul_detail")

#自定义样式，加粗
bold = workbook.add_format({'bold': 1})

#写入表头
headings = ['ip','漏洞名称','漏洞等级','漏洞类型','漏洞地址','漏洞细节','修复建议']
worksheet.write_row('A1', headings, bold)

#code banner
def get_code_banner():
    code_banner = """
      _________________________.___.            _____ __________.___ 
 /   _____/\__    ___/\__  |   |           /  _  \\______   \   |
 \_____  \   |    |    /   |   |  ______  /  /_\  \|     ___/   |
 /        \  |    |    \____   | /_____/ /    |    \    |   |   |
/_______  /  |____|    / ______|         \____|__  /____|   |___|
        \/             \/                        \/              
            
          Study Hard And Make Progress Every Day . -_-    
    """
    print code_banner

#构造header头
def create_request_header():
    user = "admin"
    security_key = "Your Security key"
    timestamp = str(int(time.time()))
    sha256 = hashlib.sha256()
    sha256.update("{0}{1}{2}".format(user, security_key, timestamp))
    token = sha256.hexdigest()
    header = {
        'user': user,
        'timestamp': timestamp,
        'token':  token,
    }
    return header

#获取单漏洞细节
def get_vul_detail(id):
    url = "https://xx.xx.xx.xx/j/risks/"+str(id)+"/"
    try:
        respon = requests.get(url, headers=create_request_header(), verify=False)
        if respon.status_code == 200:
            result = json.loads(respon.text)
        return result
    except:
        result = []
        return result   

#整理想要的漏洞字段
def select_vul_detail(vul_select,vul_list):
    try:
        vul_select.append(vul_list['data']['ip'])
        vul_select.append(vul_list['data']['risk_name'])
        vul_select.append(vul_list['data']['risk_level'])
        vul_select.append(vul_list['data']['vuln_type'])
        vul_select.append(vul_list['data']['req_url'])
        vul_select.append(vul_list['data']['vuln_detail'])
        vul_select.append(vul_list['data']['repair_advice'])
        return vul_select
    except:
        vul_select = []
        return vul_select

#写入需要的漏洞细节
def write_vul_detail(row_id, vul_select):
    worksheet.write_row('A'+str(row_id),vul_select)

#进度条展示
def get_progress_bar(id,num):
    '''
    s1 = "\r[%s%s]%d%%"%("*"*num," "*(100-num),num)
    sys.stdout.write(s1)
    sys.stdout.flush()
    '''
    percent = 1.0 * id / num * 100
    #print 'complete percent:' + str(percent) + '%', 
    print 'complete percent:%.2f' % percent + '%',   
    sys.stdout.write("\r")
    time.sleep(0.1)   

if __name__== "__main__":

    #中文数据解码输出
    #print json.dumps(get_vul_details(), encoding='utf-8', ensure_ascii=False)
    get_code_banner()

    num = 1
    row_id = 2
    vul_select = []
    #此次扫描出的漏洞总数
    vul_nums = 22
    #此次最小的漏洞id
    vul_min_id = 3982
    #此次最大的漏洞id
    vul_max_id = 4003

    #循环遍历输出所有漏洞细节
    for id in range(vul_min_id,vul_max_id+1):
        vul_list = get_vul_detail(id)
        vul_select_1 = select_vul_detail(vul_select, vul_list)
        write_vul_detail(row_id, vul_select_1)
        #print str(id)+':'+str(json.dumps(vul_select, encoding='utf-8', ensure_ascii=False))
        vul_select[:] = []
        #id = id+1
        row_id = row_id+1
        
        #进度展示
        get_progress_bar(num, vul_nums)
        num = num+1

    #print "complete percent:100.00%"     
    #print
    #f.close()
    workbook.close()
    print "Vulnerabilities Output Completed"
