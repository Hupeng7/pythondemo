#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1321781093@qq.com"
mail_pass = "rmigeehtpkjphgfg"

sender = "1321781093@qq.com"
receivers = ["1321781093@qq.com", "171956781@qq.com", "244010036@qq.com"]

msg_text = "hello world,let us go!!!"  # 需要发送的内容
charset = 'utf-8'

message = MIMEText(msg_text, 'plain', charset)
message['From'] = Header("Python Study Group", charset)
message['To'] = Header("coder", charset)

subject = "Python Study Group Share"
message['Subject'] = Header(subject, charset)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 发件人邮箱中的SMTP服务器，端口是25 [另一个用的是465，可能这个内部做了转换]
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "mail send success"
except smtplib.SMTPException:
    print "Error: mail send fail"
