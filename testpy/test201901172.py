# -*- coding: UTF-8 -*-
def char2num(s):
    #将s中的元素作为key，在0-9中取出对应的value
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print map(char2num,'13579')
def fn(x,y):
    return x*10+y
print reduce(fn,map(char2num,'13579'))


def prod(x,y):
    return x*y
print reduce(prod,[1,2,3,4])
#输出奇数
def is_odd(n):
    if n%2==1:
        return n
print filter(is_odd,[1,2,3,4,5])

#输出素数
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
print filter(is_prime,range(1,100))
