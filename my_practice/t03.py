#coding=utf-8

'''
字符串常用函数
.find(), .index(), isalpha(), isalnum(), isdigit(),
.count(), .endwith, .startwith(), .split(), 切片[start:end:step],
.encode("utf-8"), decode('utf-8'), eval(), .replace(), .strip()
ord()  chr()

'''
# 列表
# list = ['a','b','c','d','e',1,2,3]
# list.append("g")
# list.remove("c")
# list.insert(3, 'j')
# list.extend(['r','t'])
# del list[1]
# list.pop(-2)
# print list
# 
# list.sort(reverse=True)
# print list
# 
# tuple_=('a','b','c')
# 
# dict_ = {"key1":"value1","key2":"value2","list":[1,2],"sd":{"df":"gh"}}
# print dict_
# print dict_.has_key("sd")
# print dict_.has_key("df")
# # keys,values,items
# dict_.pop("key1")
# dict_.popitem()
# print dict_

# set集合
# l = (66,66,1000,"hello","hi",12,"hello")
# l = "abcdefgaaaacccc"
# l = set(l) # 数组去重
# print type(l)
# print l
# l.update("hey")  # 只能接收字符串，添加字符串到set里面，并且把字符串拆散成单个字符，还把重复的去掉
# print l
# l.add(666)  # 添加元素到集合里面
# print l
# l.pop()    # 删除set集合里面的第一个元素,不可以传参
# print l
# l.remove(666) # 删除摸个指定值
# print l
# l = frozenset(l)  # 使集合变得不可被修改
# print l
#  
# l = [4,7,1,1,9,9,4,5,2]
# l = set(l)
# print l
# l = list(l)
# l.sort(reverse=True)
# print l
# 
a = 10
print type(a)
a = long(a)
print type(a)
a = float(a)
print type(a),a
a = str(a)
print type(a)
print a+"10"
a = list(a)
print type(a),a
a = tuple(a)
print type(a),a

  
a = dict(([4,5],[6,['a','b']]))
print a
  
s = "{1:2}"
s = eval(s)
print s,type(s)
s1 = "2 if 1>3 else 2"
print eval(s1)

















