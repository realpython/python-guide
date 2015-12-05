# execly.py
#
# Example of generating code and executing it with exec()
# in the context of descriptors/metaclasses

from inspect import Parameter, Signature
import re
from collections import OrderedDict

# Utility functions
def _make_init(fields):
    '''
    Give a list of field names, make an __init__ method
    '''
    code = 'def __init__(self, %s):\n' % \
        ','.join(fields)

    for name in fields:
        code += '    self.%s = %s\n' % (name, name)
    return code

def _make_setter(dcls):
    code = 'def __set__(self, instance, value):\n'
    for d in dcls.__mro__:
        if 'set_code' in d.__dict__:
            for line in d.set_code():
                code += '    ' + line + '\n'
    return code

class DescriptorMeta(type):
    def __init__(self, clsname, bases, clsdict):
        if '__set__' not in clsdict:
            code = _make_setter(self)
            exec(code, globals(), clsdict)
            setattr(self, '__set__', clsdict['__set__'])
        else:
            raise TypeError('Define set_code(), not __set__()')

class Descriptor(metaclass=DescriptorMeta):
    def __init__(self, name=None):
        self.name = name

    @staticmethod
    def set_code():
        return [
            'instance.__dict__[self.name] = value'
            ]

    def __delete__(self, instance):
        raise AttributeError("Can't delete")

class Typed(Descriptor):
    ty = object
    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.ty):',
            '    raise TypeError("Expected %s" % self.ty)'
            ]

# Specialized types
class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

# Value checking
class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '    raise ValueError("Expected >= 0")',
            ]
        super().__set__(instance, value)

# More specialized types
class PosInteger(Integer, Positive):
    pass

class PosFloat(Float, Positive):
    pass

# Length checking
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)
        
    @staticmethod
    def set_code():
        return [
            'if len(value) > self.maxlen:',
            '    raise ValueError("Too big")',
            ]

class SizedString(String, Sized):
    pass

# Pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)
    
    @staticmethod
    def set_code():
        return [
            'if not self.pat.match(value):',
            '    raise ValueError("Invalid string")',
            ]

class SizedRegexString(SizedString, Regex):
    pass

# Structure definition code

class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):
        fields = [key for key, val in clsdict.items()
                  if isinstance(val, Descriptor) ]
        for name in fields:
            clsdict[name].name = name

        # Make the init function
        if fields:
            exec(_make_init(fields), globals(), clsdict)

        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))
        setattr(clsobj, '_fields', fields)
        return clsobj

class Structure(metaclass=StructMeta):
    pass

if __name__ == '__main__':
    class Stock(Structure):
        name = SizedRegexString(maxlen=8, pat='[A-Z]+$')
        shares = PosInteger()
        price = PosFloat()
