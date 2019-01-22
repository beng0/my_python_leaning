#coding=utf-8

def sum_():
    return 10+20
print sum_()

# 匿名函数
# a = lambda:10+20
# print a()


a = lambda:10+20
print a()
a = lambda x:x+1
print a(1)
a = lambda x: "a" if x>10 else "b"
print a(1)
a = lambda x: [i for i in range(x)]
print a(5)



lambda x: "haha" if x>10 else "wuwu"
lambda x: [i for i in range(x)]








