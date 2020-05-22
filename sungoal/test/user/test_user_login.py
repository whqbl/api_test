# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""

import unittest
import requests
import json
from config.config import *
import sys
sys.path.append('../..')
from lib.read_excel import *
from lib.case_log import log_case_info

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data_list = excel_to_list(os.path.join(data_path,'test_data.xlsx'),'TestUserLogin')

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list,'正常登陆')
        if not case_data:
            logging.error('用例数据不存在')

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, json=json.loads(data))
        log_case_info('正常登陆',url,data,expect_res,res.text)
        self.assertIn('"msg":"登录成功!"', res.text)

    def test_user_login_mobile_pw_wrong(self):
        case_data = get_test_data(self.data_list,'密码错误')
        if not case_data:
            logging.error('用例数据不存在')

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,json=json.loads(data))
        log_case_info('密码错误',url,data,expect_res,res.text)
        self.assertEqual(res.text,expect_res)

    def test_user_login_mobile_no_exist(self):
        case_data = get_test_data(self.data_list,'手机号不存在')
        if not case_data:
            logging.error('用例数据不存在')

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,json=json.loads(data))
        log_case_info('手机号不存在',url,data,expect_res,res.text)
        self.assertEqual(res.text,expect_res)


if __name__ == '__main':
    unittest.main(verbosity=2)