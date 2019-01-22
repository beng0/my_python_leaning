#coding=utf-8

#导入发送邮件的模块  smtp服务
import smtplib
#导入邮件内容的编辑模块
from email.mime.text import MIMEText
#导入带附件的邮件模块
from email.mime.multipart import MIMEMultipart
#导入邮件的头部模块
from email.header import Header

def sendEmail():
    #定义发件人的信息
    sender = "1759424517@qq.com"
    #定义我的邮箱授权码
    passwd = "krunfieyktvjdgee"
    #定义收件人的信息
    receiver = ["2397990387@qq.com","3300819387@qq.com","mr_he156@163.com"]
        
    #-------------------------------------------------------开始编辑邮件
    #定义一个带附件的邮件对象
    email = MIMEMultipart()           #邮件内容是一个字典类型
    #定义发件人  收件人  和主题内容
    email['From'] = Header('钢铁侠','utf-8')
    email['To'] = Header('金刚葫芦娃','utf-8')
    email['Subject'] = Header('世纪大战','utf-8')
    #编辑一下邮件的正文部分
    text = MIMEText("钢铁侠向葫芦娃发送挑战书","plain","utf-8")
    #将正文放入到邮件中
    email.attach(text)
    #新建一个附件
    part = MIMEText(open("E:/keyword/report.html","rb").read(),"base64","utf-8")
    #给邮件的附件命名
    part['Content-Disposition'] = "attachment;filename=20190122.html"
    #将附件添加到邮件之中
    email.attach(part)
        
    #-------------------------------------------------------开始发送邮件
    #先连接到腾讯的发送邮件服务器
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    #登陆邮件服务器
    s.login(sender, passwd)
    #发送邮件
    s.sendmail(sender,receiver,email.as_string())



















