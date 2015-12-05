# Example of application of different kinds of decorators

from debugly import debug, debugargs, debugmethods, debugattr, debugmeta

# Application of a simple decorator
@debug
def add(x, y):
    return x + y

# Application of a decorator with args
@debugargs(prefix='*** ')
def sub(x, y):
    return x - y

# Application of decorator with optional args
@debug(prefix='+++ ')
def mul(x, y):
    return x * y

# Application of a class decorator
@debugmethods
class Spam:
    def grok(self):
        pass
    def bar(self):
        pass
    def foo(self):
        pass

# Logging of attribute access
@debugattr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Application of a metaclass
class Base(metaclass=debugmeta):
    def a(self):
        pass
    def b(self):
        pass

class Grok(Base):
    def c(self):
        pass
    
class Mondo(Grok):
    def d(self):
        pass

if __name__ == '__main__':
    add(2, 3)
    sub(2, 3)
    mul(2, 3)
    s = Spam()
    s.grok()
    s.bar()

    p = Point(2,3)
    a = p.x
    b = p.y
    
    m = Mondo()
    m.a()
    m.b()
    m.c()
    m.d()

    


