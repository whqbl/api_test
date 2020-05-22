# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""

import json
import sys
from config.config import *

sys.path.append('..')

def log_case_info(casename, url, data, expect_res, res):
    if isinstance(data,dict):
        data = json.dumps(data,ensure_ascii=False) # 如果data是字典格式，转化为字符串
        logging.info("用例名称：{}".format(casename))
        logging.info("接口地址：{}".format(url))
        logging.info("接口入参：{}".format(data))
        logging.info("期望结果：{}".format(expect_res))
        logging.info("实际结果：{}".format(res))
