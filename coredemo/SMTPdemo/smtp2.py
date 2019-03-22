#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。

"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = ""  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令

sender = "1563261394@qq.com"
receivers = ['hup@hzphfin.com']  # 接受邮件

message = MIMEText('Python 邮件发送测试。。。', 'plain', 'utf-8')
message['From'] = Header("Python 学习小组", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
mesage['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender.receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
