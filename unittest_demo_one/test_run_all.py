import unittest
from unittest_demo_one.lib.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./")  # 遍历当前目录及子包中所有test_*.py中所有unittest用例

f = open("report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="测试报告",description="本测试只有用户接口",tester="niuwenjing").run(suite)
f.close()