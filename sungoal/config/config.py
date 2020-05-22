# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""

import logging
import os
import time
import pymysql

# 项目路径
prj_path = os.path.dirname(os.path.dirname(__file__)) # 当前目录
data_path = os.path.join(prj_path,'data') # 数据目录
test_path = os.path.join(prj_path,'test') # 用例目录
log_file = os.path.join(prj_path,'log','log.txt') # log文件地址
report_file = os.path.join(prj_path,'report', 'report.html') # report文件地址

print(report_file)

# log配置
logging.basicConfig(level=logging.DEBUG, # log级别
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')

# 数据库配置
db_host = '121.40.213.243'
db_port = 13306
db_user = 'root'
db_passwd = 'Sungoal@2019'
db_name = 'sungoal_customer'

# 邮箱配置
smtp_server = 'smtp.163.com'
smtp_user = 'qblwanghao@163.com'
smtp_password = 'wanghao4zhuma'
sender = smtp_user
receiver = '120073821@qq.com'
subject = 'SUNGOAL API Test Report'

