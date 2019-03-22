#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 需要现在 邮箱开通SMTP权限
my_sender = '1321781093@qq.com'  # 发件人邮箱账号
my_pass = 'rmigeehtpkjphgfg'  # 发件人邮箱密码  其实是kaile SMTP 权限的 授权码
my_user = '1321781093@qq.com'  # 收件人邮箱账号，我
yu_user = '171956781@qq.com'  # 收件人邮箱账号，土豪
dong_user = '244010036@qq.com'  # 收件人邮箱账号，栋
msg_text = '这个收件人就是土豪'


def mail():
    ret = True
    try:
        msg = MIMEText(msg_text, 'plain',
                       'utf-8')
        msg['From'] = formataddr(["FromLeo", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["土豪", yu_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "Python 学习小组"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, yu_user, dong_user], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
