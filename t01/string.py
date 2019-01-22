#coding=utf-8
str1 = 'abcdefghijklmnopqrstuvwxyz'
# print str1.find('d')
# print str1.find('dr')
# print str1.index('e')
# print str1.count('1')
# print str1.isalpha()
print str1.isdigit()
print str1.isalnum()
# str2 = 'a'
# print ord(str2)
# num1 = 78
# print chr(num1)
# print ord('0')
# print str1[::]
# print str1[::-1]
# print str1[3:7:2]
# print str1[-1:7:-2]
# print str1[-1:-7:-2]
str2 = str1.decode('utf8')
print type(str2)
str1 = str1.encode('utf8')
print type(str1)
str = '  i am mike  '
str = str.strip()
print str.strip()
print str.replace(' ', '')