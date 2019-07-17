# -*- coding: UTF-8 -*-

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print '%s %s():'% (text, func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator
@log('call')
def now():
    print 'timenow:20190128'
    print '%s %s():' % ('endcall', now.__name__)
now()

def log2(text):
    if callable(log2):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print '%s %s():' % (text, func.__name__)
                return func(*args,**kwargs)
            return wrapper()
        return decorator()
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print 'call %s():' % func.__name__
                return func(*args,**kwargs)
            return wrapper()
        return decorator()
@log2()



