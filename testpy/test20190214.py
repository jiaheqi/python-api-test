# -*- coding: UTF-8 -*-
'''
import os
#获取操作系统名称
print os.name
#获取系统所有的环境变量以dict的形式存储
print os.environ
#获取指定环境变量
print os.getenv('PATH')
#输出当前路径的绝对路径
print os.path.abspath('.')
#创建一个目录之前需要把新的目录完整显示出来，即：原本目录+新创建的目录的拼接
os.path.join('E:\Tools\pycharm\api-test-python\testpy','testdir')
print os.path.join('E:\Tools\pycharm\api-test-python\testpy','testdir')
#创建目录
#os.mkdir('testdir')
#删除目录
#os.rmdir('testdir')
#拆分路径，后一部分总是最后级别的目录或者文件名
print os.path.split('E:/Tools/pycharm/api-test-python/testpy/test1.txt')
#得到文件的扩展名
print os.path.splitext('E:/Tools/pycharm/api-test-python/testpy/test1.txt')
#重命名文件
#os.rename('test1.txt','test2.txt')
#os.remove('')
#输出当前路径下的所有目录
print [x for x in os.listdir('.')if os.path.isdir(x)]
#输出当前目录下的所有py文件
print [x for x in os.listdir('.')if os.path.isfile(x)and os.path.splitext(x)[1]=='.py']
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='jaiheqi',age=24,score=99)
#pickle.dumps()方法把任意对象序列化成一个字符串
pickle.dumps(d)
print pickle.dumps(d)
f = open('test2.txt','wb')
#把对象序列化后的str写入到文件
pickle.dump(d,f)
f.close()
#从文件中反序列化出对象，将str反序列化为对象：这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已
f1 = open('test2.txt','rb')
d = pickle.load(f1)
f1.close()
print d

import json
#将dict序列化为json
print json.dumps(d)
json_str = '{"age": 24, "score": 99, "name": "jaiheqi"}'
print json.loads(json_str)

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('bob',21,88)

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score

    }
#把student对象先序列化成dict，然后再序列化成json对象
print (json.dumps(s,default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
print (json.loads(json_str,object_hook=dict2student))

import os
print 'Process(%s)start...'%os.getpid()
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.'%(os.getpid(),os.getppid())
else:
    print 'I (%s) just created a child process (%s)'% (os.getpid(), pid)
