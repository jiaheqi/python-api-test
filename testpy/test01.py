# -*- coding: UTF-8 -*-

#年龄大于18输出成年人，否则输出
'''age=raw_input()
if age>18:
    print('adult')
else:
    print('teenager')
'''
#python不指定变量类型时候，同一个变量可以反复赋值
'''a=123
print(a)
a='abc'
print(a)
'''
#创建一个变量，并给变量赋值的时候，会在内存中创建一个变量，再创建一个字符串，然后把变量指向该字符串
'''a = 'abc'
b = a 
a = 'xyz'
print (a)
print (b)
'''
#两种除法：/：结果是浮点数，//：结果是整数
'''a = 10/3
print (a)
b = 10//3
print (b)
c = 10%3
print (c)
'''
'''
n = 123
f = 456.789
s1 = 'hello,world'
s2 = 'hello,\'adam\''
s3 = r'hello,"bart"'
print (n)
print (f)
print (s1)
print (s2)
print (s3)
print (s4)
'''

#print ('ABC'.encode('ascii'))

#print (b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#print (len('ABC'))

#print (len('中文'))

#print (ord('A'))

#print (chr(65))

#print (u'中文')

#print (u'ABC'.encode('utf-8'))

#print (u'中文'.encode('utf-8'))#转换unicode码为utf-8

#print (len(u'中文'))

#print ('abc'.decode('utf-8'))

#print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')#转换uf-8编码的为unicode码

#print ('%d-%02d'%(7,7))#%02表示在7前面补0，直到这个整数变成两位
#print ('%f-%.2f'%(0.2,0.2))
#print ('%f-%.2f'%(0.2,0.23456))#.2f表示0.23456这个小数只显示小数点后两位
#print ('Age:%s Score:%.4s Gender:%s'%(25,98.5623,True))#如果将浮点数转换为字符串时".4"表示整个字符串显示的位数
#print ('growth rate %s %%'% 7)
'''names = ['小明','小红','小强','小刚','小张']
print (names[1])
print (names[2])
print (names[-1])#输出list最后一个位置的元素
print (names[-2])#输出list倒数第二个位置的元素
names.append('小吕')#list是有序的，append默认在末位加
print (names)
for i in names:
    print i
names.pop()#删除list列表末位的元素
print (names)
for i in names:
    print i
names.insert(1,'插入')
print (names)
for i in names:
    print i

names.pop(1)#删除指定索引位置元素
print (names)
for i in names:
    print i

names[0]='小小明'#替换某个索引位置的元素，直接重新复制就好了
print (names[0])
'''
'''S = ['apple','banana',['java','php'],'pear']#二维数组
print (S[2][1])

t = (1,2)#tuple类型，被定义之后不支持修改
print(t)

sum = 0
num = range(101)
for n in num:
    sum = sum + n
print (sum)
'''
'''
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print sum

sum1 = 0
n1 = 1
while n1 < 100:
    sum1 = sum1 + n1
    n1= n1+2
print sum1

birth = int(raw_input('input birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'
'''
#字典类型dict：存储键值对
'''d = {'小明':21,'小红':22,'小张':23}
print d['小明']
print ('小明ming' in d)
print ('小明' in d)#判断key是否在dict字典中
print (d.get('小明'))
print (d.get('小明名','不存在'))

d.pop('小张')#删除dict中的key，对应的value也会被删除
'''
#set集合，只能存储key
'''s=set([1,2,3])
print s
s.add(4)
print s
s.remove(1)
print s
'''
'''
s=['c','b','a']
s.sort()#按从小到大的顺序对序列进行再排序，并且会改变原来的序列
print s
m = [1,2,3,4,6,5,7,9,8]
n=sorted(m)
print m
print n
'''
'''
a='abc'
a.replace('a','A')#replace只会修改指向的值，并不会更新变量a的值
b=a.replace('a','A')
print a
print b
'''
#abs()求绝对值函数  如果x<y，返回-1，如果x==y，返回0，如果x>y
'''
print (abs(100))
print (abs(-200))
#比较大小函数
print (cmp(1,2))
print(cmp(2,1))
'''
#数据类型转换函数
'''
print (int(100))
print (int(12.34))
print (int('123'))
print (float('12.34'))
print (str(123))
print (unicode(100))
print (bool(1))
print (bool(''))
'''
def my_abs(x):
    if x > 0:
        return 1
    else:
        return 0
print (my_abs(2))










