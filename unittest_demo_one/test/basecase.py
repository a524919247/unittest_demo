import unittest
import requests
import json
from unittest_demo.unittest_demo_one.lib.case_log import *
from unittest_demo.unittest_demo_one.config.config import *

from unittest_demo.unittest_demo_one.lib.read_excal import *


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excal_list("/Users/bytedance/Desktop/test/unittest_demo/unittest_demo_one/data/test_user_data.xlsx", "TestUserLogin")

    def get_case_data(self, case_name):
        case_date = get_test_data(self.data_list,case_name)
        if not case_date:
            return logging.error("没有找到{}用例".format(case_name))
        else:
            return case_date

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
            res = requests.post(url=url, data=eval(data))
            self.assertDictEqual(res.json(), json.loads(expect_res))

        else:
            res = requests.post(url=url, data=json.dumps(eval(data)), headers=eval(headers))
            log_case_info(case_name, url, data, expect_res, res.text)
            self.assertDictEqual(res.json(), json.loads(expect_res))


