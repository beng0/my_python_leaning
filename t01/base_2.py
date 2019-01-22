from itertools import count
list = ["apple",'orange','potato','pear']
print list
list.append('leechee')
print list
list.insert(2,45)
print list
list1 = ['tomato',89]
list.extend(list1)
print list
list.remove(89)
print list
list.pop(0)
print list
del list[1]
print list
list[2] = 'apple'
print list
