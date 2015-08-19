# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wangzhenqing <wangzhenqing1008@163.com>
# date: 2015-08-18 18:14:59

from email.mime.text import MIMEText
from email.header import Header

import smtplib


def send_email(toAdd, subject, htmlText):
    strTo = ','.join(toAdd)
    msgRoot = MIMEText(htmlText.encode('utf-8'), 'plain', 'utf-8')
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # 发送邮件
    smtp = smtplib.SMTP("smtp.126.com")
    # 设定调试级别，依情况而定
    smtp.set_debuglevel(1)
    smtp.login("wzqwsrf@126.com", "password")
    smtp.sendmail('wzqwsrf@126.com', toAdd, msgRoot.as_string())
    smtp.quit()
    return


def get_to_add():
    toAdd = ['wzqwsrf@126.com']
    return toAdd


def send_to_special(subject, htmlText):
    toAdd = get_to_add()
    send_email(toAdd, subject, htmlText)
