# -*- coding: UTF-8 -*-

'''
def foo(s):
    n = int(s)
    #如果断言失败，assert语句本身就会抛出AssertionError
    assert n!=0,'n is zero'
    return 10/n
def main():
    foo('0')
'''

'''
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
main()
'''

import codecs
with codecs.open('test1.txt','rb','gbk') as f:
    f.write('jiaheqi')

with codecs.open('test1.txt','rb','gbk') as f:
    ff=f.read()
print ff









