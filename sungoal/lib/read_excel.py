# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""


import xlrd


def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file) # 打开excel
    sh = wb.sheet_by_name(sheet) # 获取sheet工作簿
    header = sh.row_values(0) # 获取工作簿第一行数据，获取标题行数据
    for i in range(1,sh.nrows): # 跳过标题行，从第二行开始取数据
        d = dict(zip(header,sh.row_values(i))) # 将标题行和参数行打包成一个元素（字典形式）
        data_list.append(d) # 列表嵌套字典格式，每个元素是一个字典
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data
        # 如果查询不到返回none

