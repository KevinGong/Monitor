#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.MIMEText import MIMEText

mail_to="736748191@qq.com"

def send_mail(to_list,sub,content):
    mail_host="smtp.126.com"
    mail_user="linyigongguopeng@126.com"
    mail_pass="@ggp4715685"
    mail_postfix="126.com"
    me=mail_user+"<"+mail_user+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__=="__main__":
    if send_mail(mail_to,"hello","this is test"):
        print "success"
    else:
        print "fail"
