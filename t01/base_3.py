#coding=gbk

# #定义
# filename = 'd:test/111.txt'
# #打开
# file = open(filename,'w')
# #写入
# file.write('hello')
# #关闭
# file.close()


# f = 'd:test/111.txt'
# file = open(f,'a')
# file.write(' world')
# file.close()

# filename = 'd:/test/111.txt'
# file = open(filename,'w')
# for i in range(10):
#     file.write('%d\n'%(i))
# file.close()

# filename = 'd:test/111.txt'
# file = open(filename,'r')
# s = file.read()
# file.close()
# print s

# filename = 'd:test/111.txt'
# file = open(filename,'r')
# s = file.readlines()
# 
# print s[2]
# file.close()

# filename = 'd:test/111.txt'
# file = open(filename,'r')
# # s = file.readline()
# n = 0
# while n<4:
#     s = file.readline()
#     print s
#     n+=1
# file.close()


# import random

# str = ''
# f = 0
# while True:
#     n = chr(random.randint(65,90))
#     m = chr(random.randint(97,122))
#     i = random.random()
#     if f >=4:
#         break
#     if i >0.5:
#         str+=n
#     else:
#         str+=m
#     f+=1
# print str
# 
# print random.randint(1,2)

# import os
# if os.path.exists('f:/1920X1080.*'):
#     os.rename('1920X1080.*', '1024*768.*')
# str = ''
# lists = os.listdir('d:/test')
# print lists
# for i in range(len(lists)):
#     str=str+' '+lists[i]
# print str
# for i in range(len(str)):
#     if str.find('1920X1080')!=-1:
#         str = str.replace('1920X1080', '1024X768')
#         print str
# lists2 = str.split(' ')
# lists2.pop(0)
# print lists2
# print lists
# for i in range(len(lists)):
#     os.rename('d:/test/'+lists[i],'d:/test/'+lists2[i])

# import os 
# list1 = os.listdir("d:/test")
# for i in list1:
#     print i
#     list2 = i.split('.')
#     print list2
#     if list2[0] == '1920X1080':
#         os.rename('d:/test/'+i, 'd:/test/1024X768.'+list2[1])



# import hashlib
# file = open('d:/test/111.txt','rb')
# s = file.read()
# file.close()
# m = hashlib.md5(s)
# print m.hexdigest()




















