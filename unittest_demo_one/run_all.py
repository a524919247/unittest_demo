import unittest
from unittest_demo.unittest_demo_one.lib.HTMLTestReportCN import HTMLTestRunner
from unittest_demo.unittest_demo_one.config.config import *
from unittest_demo.unittest_demo_one.lib.send_email import send_email


logging.info("====================== 测试开始 =======================")

suite = unittest.defaultTestLoader.discover(test_path)  # 遍历当前目录及子包中所有test_*.py中所有unittest用例

with open(report_file, 'wb') as f:
    HTMLTestRunner(stream=f,title="测试报告",description="本测试只有用户接口",tester="niuwenjing").run(suite)
send_email(report_file)  # 发送邮件

logging.info("======================= 测试结束 =======================")