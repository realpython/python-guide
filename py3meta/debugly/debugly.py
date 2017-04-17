# debugly.py
#
# Examples of basic metaprogramming concepts.
# You know, for debugging.

from functools import wraps, partial

def debug(func):
    '''
    A simple debugging decorator
    '''
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugargs(prefix=''):
    '''
    A debugging decorator that takes arguments
    '''
    def decorate(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

def debug(func=None, *, prefix=''):
    '''
    Decorator with or without optional arguments
    '''
    if func is None:
        return partial(debug, prefix=prefix)
    
    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    '''
    Apply a decorator to all callable methods of a class
    '''
    for name, val in vars(cls).items():
        if callable(val):
            setattr(cls, name, debug(val))
    return cls

def debugattr(cls):
    '''
    Decorator that adds logging to attribute access
    '''
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__
    return cls

class debugmeta(type):
    '''
    Metaclass that applies debugging to methods
    '''
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj




    


