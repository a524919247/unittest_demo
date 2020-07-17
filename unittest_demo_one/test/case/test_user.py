import unittest
import requests
from unittest_demo_one.lib.read_excal import *
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下



# def setUpModule():
#     print('用户相关用例开始执行')
#
# def tearDownModule():
#     print('用户相关用例执行完毕')

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excal_list("test_user_data.xlsx", "TestUserLogin")

    # @classmethod
    # def tearDownClass(cls):
    #     print('用户登录执行完毕')

    # def setUp(self):  # 该类中每个测试用例执行一次
    #     print('开始执行')
    #
    # def tearDown(self):
    #     print('执行完毕')


    def test_type_error(self):
        case_data = get_test_data(self.data_list,"test_type_error")
        if not case_data:
            print("用例数据不存在")
        url = case_data['url']
        data = case_data["data"]
        expect_res = case_data['expect_res']

        res = requests.post(url = url,data = data)
        print(res.text)
        self.assertEqual(res.text, expect_res)

    def test_user_nil(self):
        case_data = get_test_data(self.data_list, "test_user_nil")
        if not case_data:
            print("用例数据不存在")
        url = case_data['url']
        data = case_data["data"]
        expect_res = case_data['expect_res']
        print(expect_res)
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=url, data=json.dumps(data),headers=headers)
        res.encoding = 'unicode_escape'
        print(res.text)
        self.assertEqual(res.text, expect_res)

    # def test_login_success(self):
    #     data = {"name":"张三","password":"123456"}
    #     headers = {"Content-Type": "application/json"}
    #     res = requests.post(url=self.url, data=json.dumps(data),headers=headers)
    #     res.encoding = 'unicode_escape'
    #     self.assertIn('登陆成功', res.text)
    #
    # def test_login_fail(self):
    #     data = {"name":"张三","password":"1234dsda56"}
    #     headers = {"Content-Type": "application/json"}
    #     res = requests.post(url=self.url, data=json.dumps(data),headers=headers)
    #     res.encoding = 'unicode_escape'
    #     self.assertIn('姓名或密码错误', res.text)
