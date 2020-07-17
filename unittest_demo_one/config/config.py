import logging
import os


# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 当前文件的绝对路径的上一级，__file__指当前文件

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log.txt')  # 每天生成新的日志文件
report_file = os.path.join(prj_path, 'report.html')  # 每次生成新的报告

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式默认为a  可设置成w


# 邮件配置
smtp_server = 'smtp.163.comm' # 邮件服务器
smtp_user = '13116150965@163.com' # 邮箱用户名
smtp_password = '#######' # 邮箱密码

sender = smtp_user  # 发件人
receiver = '524919247@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题