#coding=utf-8
from string import lstrip

# 字符串的操作
# 1.增加
str = 'asdffg'
str1 = str+'h'
print str1
print str
# 2.删
# str = str[1:1]
# print str+'h'
# 3.改
# str = str.replace('a','v')
# print str
# 4.查
print str.count('f') # 统计某个字符出现的次数
n = str.find("f") # 找到某个字符第一次出现的位置
print n
n1 = str.find("f")
print n1
print 'f' in str
print 'f' not in str
# 字符串切片
# str = str[1:4:2]
# print str

# str = str[::-1]
# print str
# str = str[-1:-4:-2]
# print str

# 其它函数
print str.upper()
print str
print str.lower()
str2 = '  sff  '
print str2.strip()
print str2
print str2.lstrip()
print str2.rstrip()
print str.split('f')
print str
print str.startswith('that') # 判断字符串是否是以某个字符作为开头
print str.endswith("g")  # 判断字符串是否是以某个字符作为结尾

str = str.encode('utf8')
print type(str)
str = str.decode('utf8')
print type(str)
str = str.encode('utf8')
print type(str)

print str.isalpha()
print str.isdigit()
print str.isalnum()

str3= 'a'
print ord(str3)
num = 97
print chr(97)

# 切片，+，*，count,replace,in,not in,isalpha,isdigit,isalnum,encode,decode,strip,lstrip
# rstrip,ord,chr,find,index














