#coding=utf-8
for i in range(4):
    print '*'*(i+1)
    
for i in range(5):
    print ' '*(4-i)+' *'*(i)
    
    
    
str = "a"
print ord(' ')

# 冒泡排序
s=0
list = [2,5,63,6,77,23,7,64,24,78,4,1]
for i in range(len(list)-1):
#     f=True
    for j in range(len(list)-i-1):
        s+=1
        if list[j] > list[j+1]:
#             f=False
            list[j],list[j+1]=list[j+1],list[j]
#     if f:
#         break
print list
print s

# 直接排序
# s=0
# for i in range(len(list)-1):
# #     flag=True
#     for j in range(i,len(list)-1):
#         if list[j]>list[j+1]:
#             index = j+1
# #             flag=False
#             s+=1
#     print s
#     list[i],list[index]=list[index],list[i]
# #     if flag:
# #         break
# print list










