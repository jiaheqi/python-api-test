# -*- coding: UTF-8 -*-

listtest=['apple','banana','orage','peach','watermelon']
tupletest=('apple','banana','orage','peach','watermelon')
string='abcdefg'
dicttest={'a':1,'b':2,'c':3,'d':4,}
#对dict的遍历，默认遍历key
for key in dicttest:
    print key
#借助itervalues()可以遍历输出dict的value
for value in dicttest.itervalues():
    print value
#字符串也是可迭代对象，也可以遍历
for i in string:
    print i
#判断一个类型是否支持迭代
from collections import Iterable
print isinstance('abc',Iterable)#字符串支持迭代
print isinstance([1,2,3],Iterable)#list也支持迭代
print isinstance(123,Iterable)#整数不支持迭代
print isinstance({'a':1,'b':2},Iterable)#dict支持迭代
print isinstance((1,2,3),Iterable)#tuple也支持迭代

#enumerate函数可以把一个list变成索引-元素对
for index,value in enumerate(listtest):
    print index,value
#列表生成式生成list
print range(0,9)
list1 = [x * x for x in range(1,11)]
print list1
print [x * x for x in range(1,11) if x % 2 == 0]
#通过两层循环生成列表
print [m+n for  m in 'abc' for n in 'ABC']
import os
print [d for d in os.listdir('.') ]#list可以列出文件和目录
#列表生成式也可以使用两个变量来生成list
for  k,v in dicttest.iteritems():
    print k,'=',v
#判断一个变量是不是字符串
print isinstance(string,str)
print isinstance(list1,str)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
fib(6)

def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for n in fib2(6):
    print n
#方法：把一个函数作用于一个新的序列
def f(x):
    return x * x
print map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])

def add(x,y):
    return x+y
print reduce(add,[1,3,5,7,9])

def char2num(s):
    return  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print map(char2num,'13579')