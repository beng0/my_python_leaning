#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "1759424517@qq.com"
passwd = "krunfieyktvjdgee"
receiver = ["2397990387@qq.com","3300819387@qq.com","mr_he156@163.com"]

email = MIMEMultipart()
email["From"] = Header('小小','utf-8')
email["To"] = Header('大大先生','utf-8')
email["Subject"] = Header('榜样东西','utf-8')

text = MIMEText("我的第一封邮件","plain","utf-8")
email.attach(text)

part = MIMEText(open("E:/keyword/report.html","rb").read(),"base64","utf-8")
part["Content-Disposition"]="attachment;filename=report.html"
email.attach(part)

s = smtplib.SMTP_SSL("smtp.qq.com",465)
s.login(sender, passwd)
s.sendmail(sender,receiver,email.as_string())











