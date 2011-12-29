Picking an Interpreter
======================

Which Python to use?


2.x vs 3.x
~~~~~~~~~~

**tl;dr**: Python 2.x is the status quo, Python 3.x is the shiny new thing.


`Further Reading <http://wiki.python.org/moin/Python2orPython3>`_


Today
-----

If you're choosing a Python interpreter to use, I *highly* recommend you Use Python 2.7.x, unless you have a strong reason not to.


The Future
----------

As more and more modules get ported over to Python3, the easier it will be for
others to use it.


Which Python to Support?
~~~~~~~~~~~~~~~~~~~~~~~~

If you're starting work on a new Python module, I recommend you write it for
Python 2.5 or 2.6, and add support for Python3 in a later iteration.

Implementations
~~~~~~~~~~~~~~~

There are several popular implementations of the Python programming language on
different back-ends.

CPython
-------

`CPython <http://www.python.org>`_ is the reference implementation of Python,
written in C. It compiles Python code to intermediate bytecode which is then
interpreted by a virtual machine. When people speak of *Python* they often mean
not just the language but also this implementation. It provides the highest
level of compatibility with Python packages and C extension modules.

If you are writing open-source Python code and want to reach the widest possible
audience, targeting CPython is your best bet. If you need to use any packages
that are rely on C extensions for their functionality (eg: numpy) then CPython
is your only choice.

Being the reference implementation, all versions of the Python language are
available as CPython. Python 3 is only available in a CPython implementation.

PyPy
----

`PyPy <http://pypy.org/>`_ is a Python interpreter implemented in a restricted
statically-typed subset of the Python language called RPython. The interpreter
features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).

PyPy aims for maximum compatibility with the reference CPython implementation
while improving performance.

If you are looking to squeeze more performance out of your Python code, it's
worth giving PyPy a try.

Currently PyPy supports Python 2.7.

Jython
------

`Jython <http://www.jython.org/>`_ is a Python implementation that compiles
Python code to Java byte code that then executes on a JVM. It has the additional
advantage of being able to import and use any Java class the same as a Python
module.

If you need to interface with an existing Java codebase or have other reasons to
need to write Python code for the JVM, Jython is the best choice.

Currently Jython supports up to Python 2.5.

IronPython
----------

`IronPython <http://ironpython.net/>`_  is an implementation of Python for .NET
framework. It can use both Python and .NET framework libraries, and can also
expose Python code to other .NET languages.

`Python Tools for Visual Studio <http://ironpython.net/tools/>`_ integrate
IronPython directly in to the Visual Studio development environment, making it
an ideal choice for Windows developers.

IronPython supports Python 2.7.
