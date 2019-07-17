# -*- coding: UTF-8 -*-
'''
try:
    print 'try...'
    r = 10/2
    print 'result',r
except ZeroDivisionError,e:
    print 'except',e
finally:
    print 'finally'
print 'END'
'''

'''
try:
    print 'try...'
    r = 10/int('a')
    print 'result',r
except ValueError,e:
    print 'ValueError',e
except ZeroDivisionError,e:
    print 'ZeroDivisionError',e
else:
    print 'no error'
finally:
    print 'finally...'
print 'END'
'''
'''
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except StandardError,e:
        print 'Error'
    finally:
        print 'finally...'
'''

import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except StandardError,e:
        logging.exception(e)
main()
print 'END'