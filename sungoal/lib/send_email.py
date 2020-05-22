# -- coding:utf-8 --
"""
@author: wangh
@file: 
@time: 
@desc:
"""

# import smtplib  # 用于建立smtp连接
# from email.mime.text import MIMEText  # 邮件需要专门的MIME格式
#
# # 1. 编写邮件内容（Email邮件需要专门的MIME格式）
# msg = MIMEText('this is a test email', 'plain', 'utf-8')  # plain指普通文本格式邮件内容
#
# # 2. 组装Email头（发件人，收件人，主题）
# msg['From'] = 'test_results@sina.com'  # 发件人
# msg['To'] = '2375247815@qq.com'  # 收件人
# msg['Subject'] = 'Api Test Report'  # 邮件主题
#
# # 3. 连接smtp服务器并发送邮件
# smtp = smtplib.SMTP_SSL('smtp.sina.com')  # smtp服务器地址 使用SSL模式
# smtp.login('test_results@sina.com', 'hanzhichao123')  # 用户名和密码
# smtp.sendmail("test_results@sina.com", "2375247815@qq.com", msg.as_string())
# smtp.quit()


import smtplib # 用于建立smtp连接
from email.mime.text import MIMEText # 邮件需要专门的MIME格式
from email.mime.multipart import MIMEMultipart # 混合MIME格式，支持上传附件
from email.header import Header # 用于使用中文邮件主题
from config.config import *
import sys
import time
sys.path.append('..')

def send_email(report_file):
    msg = MIMEMultipart() # 混合MIME格式
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8')) # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = sender # 发件人
    msg['To'] = receiver # 收件人
    msg['Subject'] = Header(subject, 'utf-8') # 邮件主题
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8') # 二进制格式打开
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="test_report_{}.html"'.format(time.strftime('%Y-%m-%d %H:%M:%S')) # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server) # smtp服务器地址，使用ssl模式
        smtp.login(smtp_user,smtp_password) # 用户名和密码
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info('邮件发送完成！')
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

