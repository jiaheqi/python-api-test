# -*- coding: UTF-8 -*-

list1=['bob', 'about', 'Zoo', 'Credit']
def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(list1,cmp_ignore_case)


def lazy_sum(*args):

    def sum():
        ax = 0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,2,3,4)
print f #调用f返回的是sum函数
print f()#调用f（）方法，返回的是函数返回值

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print f1()
print f2()
print f3()

#匿名函数

print map(lambda x:x*x,[1,2,3,4,5])

f=lambda x:x*x
print f(5)
