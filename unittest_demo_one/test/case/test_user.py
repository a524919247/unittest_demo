import unittest
import requests
import json
from unittest_demo.unittest_demo_one.test.basecase import BaseCase




# def setUpModule():
#     print('用户相关用例开始执行')
#
# def tearDownModule():
#     print('用户相关用例执行完毕')

class TestUserLogin(BaseCase):

    # @classmethod
    # def setUpClass(cls):  # 整个测试类只执行一次
    #     cls.data_list = excal_list("test_user_data.xlsx", "TestUserLogin")

    # @classmethod
    # def tearDownClass(cls):
    #     print('用户登录执行完毕')

    # def setUp(self):  # 该类中每个测试用例执行一次
    #     print('开始执行')
    #
    # def tearDown(self):
    #     print('执行完毕')


    def test_type_error(self):
        """参数类型错误"""
        case_date = self.get_case_data("test_type_error")
        self.send_request(case_date)

    def test_user_nil(self):
        """登录条件缺失"""
        case_date = self.get_case_data("test_user_nil")
        self.send_request(case_date)


    def test_login_success(self):
        """登陆成功"""
        case_date = self.get_case_data("test_login_success")
        self.send_request(case_date)

    def test_login_fail(self):
        """姓名或密码错误"""
        case_date = self.get_case_data("test_login_fail")
        self.send_request(case_date)
