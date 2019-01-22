#coding=utf-8

for i in range(1,10):
    for j in range(1,i+1):
        print '{1}*{0}={2}'.format(i, j,i*j),
    print ''

for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print '%d*%d=%d'%(j,i,i*j),
    print ''