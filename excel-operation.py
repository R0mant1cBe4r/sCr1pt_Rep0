#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import xlwt


#读取excel
def excel_read(path):
    table = xlrd.open_workbook(path).sheet_by_index(0) # 0 表示获取第一个工作页
    #nrows = table.nrows #行总数
    #ncols = table.ncols #列总数

    #row_data = table.row_values(0)  #获得第1行的数据列表
    #col_data = table.col_values(0)  #获得第1列的数据列表

    return table

'''    
#创建new excel 创建工作页
def excel_create(path):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet  = workbook.add_sheet('info')
    #workbook.save(path)
    return workbook, worksheet 
'''

if __name__ == '__main__':
    arr = []
    table = excel_read("test.xls")
    nrows = table.nrows #行总数
    #print nrows
    ncols = table.ncols #列总数

    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet  = workbook.add_sheet('info')    
    
    for i in range(0,nrows):
        #cell_value1 = table.cell_value(i,0)   #每一行的第一格
        #cell_value2 = table.cell_value(i,0)   #每一行的第二格
        #cell_value3 = table.cell_value(i,0)   #每一行的第三格
        #...
        #...
        #arr.append(cell_value1)
        values_row = table.row_values(i)  #读取每行内容
        #print values_row


        for s in range(len(values_row)):
            worksheet.write(i, s, values_row[s])
            
    workbook.save("te.xls")
