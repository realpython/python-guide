# importly.py
#
# Addition of an import hook to make it possible to 
# import XML-structure specifications directly

from inspect import Parameter, Signature
import re
from collections import OrderedDict
from xml.etree.ElementTree import parse
import os

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

# Import hooks
def _xml_to_code(filename):
    doc = parse(filename)
    code = 'import importly as _i\n'
    for st in doc.findall('structure'):
        code += _xml_struct_code(st)
    return code

def _xml_struct_code(st):
    stname = st.get('name')
    code = 'class %s(_i.Structure):\n' % stname
    for field in st.findall('field'):
        name = field.text.strip()
        dtype = '_i.' + field.get('type')
        kwargs = ', '.join('%s=%s' % (key, val)
                           for key, val in field.items()
                           if key != 'type')
        code += '    %s = %s(%s)\n' % (name, dtype, kwargs)
    return code

class StructImporter:
    def __init__(self, path):
        self._path = path

    def find_module(self, fullname, path=None):
        name = fullname.rpartition('.')[-1]
        if path is None:
            path = self._path
        for dn in path:
            filename = os.path.join(dn, name+'.xml')
            if os.path.exists(filename):
                return StructXMLLoader(filename)
        return None

import imp
class StructXMLLoader:
    def __init__(self, filename):
        self._filename = filename
        
    def load_module(self, fullname):
        mod = sys.modules.setdefault(fullname,
                                     imp.new_module(fullname))
        mod.__file__ = self._filename
        mod.__loader__ = self
        code = _xml_to_code(self._filename)
        exec(code, mod.__dict__, mod.__dict__)
        return mod

import sys
def install_importer(path=sys.path):
    sys.meta_path.append(StructImporter(path))

if __name__ == '__main__':
    install_importer()
    import datadefs
    s = datadefs.Stock('GOOG', 100, 490.1)
    p = datadefs.Point(2,3)
    h = datadefs.Address('www.python.org', 80)
