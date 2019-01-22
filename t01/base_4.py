#coding=utf-8
# def fruit(fru):
#     menu={"apple":19,"pear":10,"banana":8}
#     if fru in menu.keys():
#         print '%s的价格是%d元'%(fru,menu[fru])
#     else:
#         print '你输入的水果不存在'
#     return
# 
# fru = raw_input('请输入一种水果：')
# fruit(fru)


# class cal():
#     def __init__(self,*x):
#         self.x = x
#     def sum_(self):
#         sum = 0
#         for i in self.x:
#             if type(i) in [int,float,long]:
#                 sum += i
#         return sum
#     
#     def sub_(self):
#         s = self.x[0]
#         for i in range(1,len(self.x)):
#             if type(self.x[i]) in [int,float,long]:
#                 s = s - self.x[i]
#             return s
#     def mul_(self):
#         return
#     def chu_(self):
#         return



# x = 100
# def test():
#     global x
#     x = 20
# #     print x
#     return
#     
# test()
    
# print x

# _y = 100
# 
# __z = 120
#             

# 
# class Birds():
#     def talk_(self):
#         return 'gugu'
#     
#     def _eat_(self):
#         return '吃谷子'
#     
#     def __sleep(self):
#         return '躺着睡觉'
# 
# class CuiNiao(Birds):
#     def _eat_(self):
#         return '吃鱼'
#     def __sleep(self):
#         return '不睡觉'
# 
# class salary():
#     def __init__(self):
#         self.s = 0
#     def __set_salary(self):
#         self.s = 10000
#     def get_salary(self):
#         self.__set_salary()
#         return self.s
    

# practice
# 类的定义
# class Animal():
#     def talk(self):
#         print "嚎叫"
#     
#     def eat(self):
#         print "吃东西"
#     
#     def sleep(self):
#         print '睡觉咯'
# 
# # 类的继承
# class Tigle(Animal):
#     def talk(self):
#         print "嗷呜嗷呜"
#     def walk(self):
#         print "漫步"
        
# 类的构造函数

# class Cal():
#     def __init__(self,*x):
#         self.x = x
#     def sum(self):
#         x = self.x   
#         s = 0
#         for i in x:
#             if type(i) in [int,float,long]:
#                 s += i
#         return s
#     def sub(self):
#         s = self.x[0]
#         print s
#         for i in range(1,len(self.x)):
#             if type(self.x[i]) in [int,float,long]:
#                 s = s - self.x[i]
#         return s 
        
# 类里面值的传递  self.
# 类里面的变量
# class Salary():
#     def __set_salary(self):
#         self.s = 10000
#     def get_salary(self):
#         self.__set_salary()
#         return self.s


# 函数

def fruit(fruit='apple',*fru):
    if fru == ():
        return fruit
    else:
        return fru
print fruit('orange')

# def sum_3(**x):
#     return x
# print sum_3({1:2})















        
    

    
        