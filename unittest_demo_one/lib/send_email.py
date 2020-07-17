import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from unittest_demo.unittest_demo_one.config.config import *


# 编写邮件内容（Email邮件需要专门的MIME格式）
def send_email(report_file):

    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    # 组装Email的部分
    msg['From'] = 'test_results@sina.com'  # 发件人
    msg['To'] = '2375247815@qq.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题

    # 构造附件，传送当前目录下的文件
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    # 连接smtp服务器并发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password)  # 用户名和密码
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
        smtp.quit()
    except Exception as e:
        logging.error(str(e))
