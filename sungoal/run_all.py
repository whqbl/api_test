# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""

import unittest
from config.config import *
from lib.send_email import send_email
from lib.HTMLTestReportCN import HTMLTestRunner

logging.info('================================== 测试开始 ==================================')

suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f, title='API Test', description='API Test Report', tester='WangH').run(suite)

# send_email(report_file)

logging.info('================================== 测试结束 ==================================')