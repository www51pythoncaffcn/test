#!/usr/bin/env python3
# -*- coding: utf-8-*-
from email.mime.text import MIMEText    
import smtplib
from email.header import Header

#一、构建邮件内容：正文+邮件表头（来自谁，发给谁，主题）

#1、邮件正文
text = "你好，我的第2封邮件"    
message= MIMEText(text,'plain', 'utf-8') 
#2、邮件表头
message['From']=Header('老公','utf-8')
message['To']=Header('爱人','utf-8')
subject = '定时给你发邮件'
message['Subject'] = Header(subject, 'utf-8')

#二、发送邮件：1、链接MTA发送服务器 2、登陆你的账号和密码  3、发送邮件（谁发、发给谁，邮件内容格式化）

smtp = smtplib.SMTP() 
smtp.connect('smtp.exmail.qq.com',25) 
smtp.login('@账号', '@密码') 
smtp.sendmail('@账号', '@账号', message.as_string()) 
smtp.quit()
print('邮件发送成功！')