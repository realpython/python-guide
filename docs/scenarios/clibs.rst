Interfacing with C/C++ Libraries
================================


ctypes
------

`ctypes <https://docs.python.org/3/library/ctypes.html>`_ is the de facto
library for interfacing with C/C++, and it provides not only full access to
the native C interface of most major operating systems (e.g., kernel32 on
Windows, or libc on *nix), but also provides support for loading and
interfacing with dynamic libraries, such as DLLs or shared objects at runtime.
It does bring along with it a whole host of types for interacting with system
APIs, and allows you to rather easily define your own complex types, such
as structs and unions, and allows you to modify things such as padding and
alignment, if needed. It can be a bit crufty to use, but in conjunction with
the `struct <https://docs.python.org/3.5/library/struct.html>`_ module, you
are essentially provided full control over how your data types get translated
into something something usable by a C(++).

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
