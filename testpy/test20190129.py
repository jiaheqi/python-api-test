# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.__name = name#前面加下划线，可以防止外部实例随意修改属性值
        self.__score = score
    def printscore(self):
        print '%s %s'% (self.__name,self.__score)
    def getgrade(self):
        if self.__score > 80:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return '不及格'
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad error')

class Animal(object):
    def run(self):
        print'animal is running'

class Dog(Animal):
    def run(self):
        print 'dog is running'
class Cat(Animal):
    def run(self):
        print 'cat is running'
def run_two(animal):
    animal.run()
    animal.run()

bart = Student('xiaoming',99)
print bart.get_name()
print bart.get_score()
print bart.printscore()
print bart.getgrade()

dog = Dog()
cat = Cat()
dog.run()
cat.run()
run_two(Animal())
run_two(Dog())
run_two(Cat())
