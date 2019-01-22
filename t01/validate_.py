#coding=utf-8
import random
str1='abcdefghijklmn1234567890'
str2=''
while True:
    if len(str2)==4:
        break
    index = random.randint(1,len(str1)-1)
    if str2.find(str1[index])==-1:
        str2+=str1[index]
print str2
a = raw_input('请输入验证码：')
if a == str2:
    print '输入正确'
else:
    print '输入错误'