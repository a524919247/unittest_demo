import unittest
import requests
import json
from unittest_demo.unittest_demo_one.lib.case_log import *
from unittest_demo.unittest_demo_one.config.config import *

from unittest_demo.unittest_demo_one.lib.read_excal import *


class BaseCase(unittest.TestCase):
    # 每次调用时获取到EXCAL中的数据（每个类只执行一次）
    @classmethod
    def setUpClass(cls):
        cls.data_list = excal_list("/Users/bytedance/Desktop/test/unittest_demo/unittest_demo_one/data/test_user_data.xlsx", "TestUserLogin")

    # 通过case_name获取到case数据
    def get_case_data(self, case_name):
        case_data= get_test_data(self.data_list,case_name)
        if not case_data:
            return logging.error("没有找到{}用例".format(case_name))
        else:
            return case_data

    # 通过获取到case_data发送方对应请求
    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        data = case_data.get('data')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get("method")
        data_type = case_data.get("data_type")

        if method == "GET":
            pass

        elif data_type == "FROM":
            res = requests.post(url=url, data=eval(data))   # 将字符串转换为字典
            log_case_info(case_name, url, data, expect_res, res.text)   # 打印对应日志
            self.assertDictEqual(res.json(), json.loads(expect_res))    # 断言

        else:
            res = requests.post(url=url, data=json.dumps(eval(data)), headers=eval(headers))
            log_case_info(case_name, url, data, expect_res, res.text)
            self.assertDictEqual(res.json(), json.loads(expect_res))


