# -*- coding: UTF-8 -*-

class Student(object):
    __slots__ = ('name','age')#限制类的属性，只允许该类的实例绑定显示的属性，对别的属性不能进行绑定

def set_age(self,age):
    self.age=age
s = Student()

def set_score(self,score):
    self.score=score



from types import MethodType
s.set_age=MethodType(set_age,s,Student)#给s实例绑定一个set_age方法，但是对别的Student实例不生效
s.set_age(24)
print s.age
Student.set_score=MethodType(set_score(),None,Student)#给一个类绑定一个set_score方法，对该类的实例都生效

#birth是可读写的属性，age是只读的属性
class User(object):
    @property#相当于设置了一个getter方法
    def birth(self):
        return self._birth
    @birth.setter#相当于设置了一个setter方法
    def birth(self,value):
        self.birth=value
    @property
    def age(self):
        return self.age
u = User()
u.birth=1995
print u.birth
print


