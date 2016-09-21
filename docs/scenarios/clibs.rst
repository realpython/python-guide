Interfacing with C/C++ Libraries
================================

C Foreign Function Interface
----------------------------

`CFFI <https://cffi.readthedocs.io/en/latest/>`_ provides a simple to use
mechanism for interfacing with C from both CPython and PyPy. It supports two
modes: an inline ABI compatibility mode (example provided below), which allows
you to dynamically load and run functions from executable modules (essentially
exposing the same functionality as LoadLibrary or dlopen), and an API mode,
which allows you to build C extension modules.

ABI Interaction
~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    from cffi import FFI
    ffi = FFI()
    ffi.cdef("size_t strlen(const char*);")
    clib = ffi.dlopen(None)
    length = clib.strlen("String to be evaluated.")
    # prints: 23
    print("{}".format(length))

ctypes
------

`ctypes <https://docs.python.org/3/library/ctypes.html>`_ is the de facto
library for interfacing with C/C++ from CPython, and it provides not only
full access to the native C interface of most major operating systems (e.g.,
kernel32 on Windows, or libc on \*nix), but also provides support for loading
and interfacing with dynamic libraries, such as DLLs or shared objects at
runtime. It does bring along with it a whole host of types for interacting
with system APIs, and allows you to rather easily define your own complex
types, such as structs and unions, and allows you to modify things such as
padding and alignment, if needed. It can be a bit crufty to use, but in
conjunction with the `struct <https://docs.python.org/3.5/library/struct.html>`_
module, you are essentially provided full control over how your data types get
translated into something usable by a pure C(++) method.

Struct Equivalents
~~~~~~~~~~~~~~~~~~

:file:`MyStruct.h`

.. code-block:: c
    :linenos:

    struct my_struct {
        int a;
        int b;
    };

:file:`MyStruct.py`

.. code-block:: python
    :linenos:

    import ctypes
    class my_struct(ctypes.Structure):
        _fields_ = [("a", c_int),
                    ("b", c_int)]

SWIG
----

`SWIG <http://www.swig.org>`_, though not strictly Python focused (it supports a
large number of scripting languages), is a tool for generating bindings for
interpreted languages from C/C++ header files. It is extremely simple to use:
the consumer simply needs to define an interface file (detailed in the
tutorial and documentations), include the requisite C/C++ headers, and run
the build tool against them. While it does have some limits, (it currently
seems to have issues with a small subset of newer C++ features, and getting
template-heavy code to work can be a bit verbose), it provides a great deal
of power and exposes lots of features to Python with little effort.
Additionally, you can easily extend the bindings SWIG creates (in the
interface file) to overload operators and built-in methods, effectively re-
cast C++ exceptions to be catchable by Python, etc.

Example: Overloading __repr__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:file:`MyClass.h`

.. code-block:: c++
    :linenos:

    #include <string>
    class MyClass {
    private:
        std::string name;
    public:
        std::string getName();
    };

:file:`myclass.i`

.. code-block:: c++
    :linenos:

    %include "string.i"

    %module myclass
    %{
    #include <string>
    #include "MyClass.h"
    %}

    %extend MyClass {
        std::string __repr__()
        {
            return $self->getName();
        }
    }

    %include "MyClass.h"


Boost.Python
------------

`Boost.Python <http://www.boost.org/doc/libs/1_59_0/libs/python/doc/>`_
requires a bit more manual work to expose C++ object functionality, but
it is capable of providing all the same features SWIG does and then some,
to include providing wrappers to access PyObjects in C++, extracting SWIG-
wrapper objects, and even embedding bits of Python into your C++ code.
