#coding=utf-8

# num = 2
# if num%2 == 0:
#     print '{}是偶数'.format(num)
# if num%2 == 1:
#     print '%d是奇数'%(num)

# str = 'hello'
# flag = False
# list = ['apple','pear','helloo']
# for n in range(len(list)):
#     if list[n] == str:
#         print '有这个数了'
#         flag = True
#         break
# if flag == False:
#     list.append(str)
# print list
#     

'''
dict1 = {"apple":18,"pear":16,"orange":10}
fruit = raw_input("请输入一种水果:")
if dict1.has_key(fruit):
    print '这个水果%d元'%(dict1[fruit])
else:
    print '没有这种水果'
'''
# print '哈哈'
# num1 = 2.3
# print type(num1)
# str1 = raw_input('请输入：')
# if str1.isdigit() == True:
#     if type(str1) == "<type 'float'>":
#         print "这个数是浮点数"
# else:
#     print "不是浮点数"

# l = []
# for i in range(1,100):
#     if i % 2 == 1:
#         l.append(i)
# print l
# for i in enumerate([1,2,3]):
#     print i
    
# 鸡兔同笼
# 鸡i只，兔j只
# for i in range(35):
#     for j in range(35):
#         if i+j == 35 and i*2+j*4 == 94:
#             print '鸡%d只，兔%d只'%(i,j)
#             break


    
# 直接排序 
# l = [8,0,3,9,4,2,7,1]
# for i in range(len(l)):
#     index = i
#     for j in range(i,len(l)-1):
#         if l[index]>l[j+1]:
#             index = j+1
#     l[i],l[index] = l[index],l[i]
# print l

# 冒泡排序
# l = [8,0,3,9,4,2,7,1]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print l
# import math
# for i in xrange(1,100):
#     total = 8*2**i
#     if total >=8848000:
#         print i
#         break

# 假设买公鸡n只，母鸡m只，小鸡l只
# t = 0
# for n in range(50):
#     for m in range(100):
#         for l in range(200):
#             if 2*m+n+l/2 == 100 and m!=0 and n!=0 and l!=0 and m+n+l==100:
# #                 print m,n,l
#                 t+=1
# print t
# n=0
# for i in range(1900,2019):
#     if (i%4==0 and i%100!=0) or i%400 == 0:
#         n+=1
#         print i
# print n

# 每次弹起的高度为 m,第n次弹起高度为m=100/(2n)
# 第i次弹起的总高度为，t=100*2+(100/(2**i))*2

# h=100
# s=0
# for i in range(0,10):
#     s += h*(0.5**i)+h*(0.5**(i+1))
#     print h
# # t+=0.097625
# 
# print s

# 打印三角形
for i in range(1,5):
    print '*'*i
    
for i in range(1,5):
    print ' '*(4-i)+'*'*i+' '*(4-i)+'*'*i
