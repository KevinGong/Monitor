#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.MIMEText import MIMEText
import sys
def mail_who(ip):
    f = file("conf/sms_send.conf",'r')
    d = {}
    i = f.readline()
    while i:
       d[i.split('#')[0]] = i.split('#')[1].split(',')
       i = f.readline()
    try:
      return d[ip]
    except Exception,e:
      return e

def send_mail(to_list,sub,content):
    mail_host="smtp.126.com"
    mail_user="linyigongguopeng@126.com"
    mail_pass="@ggp4715685"
    mail_postfix="126.com"
    me=mail_user+"<"+mail_user+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ','.join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception, e:
        return False
if __name__=="__main__":
    mail_t = mail_who(sys.argv[1]) 
    if send_mail(mail_t,"hello",sys.argv[2]):
        print "success"
    else:
        print "fail"
    print mail_who(str(sys.argv[1]))
