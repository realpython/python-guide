Picking an Interpreter
======================

.. _which-python:

Today (Python 2)
~~~~~~~~~~~~~~~~

If you're choosing a Python interpreter to use, I *highly* recommend you use
Python 2.7.x, unless you have a strong reason not to.

Also use Python 2.7.x if you're starting to work on a new Python module. If you
have managed to get it working on 2.7, you can add support for older 2.x
versions.

The Future (Python 3)
~~~~~~~~~~~~~~~~~~~~~

    Python 2.x is the status quo, Python 3.x is the shiny new thing.

`Further Reading <http://wiki.python.org/moin/Python2orPython3>`_

The difference between Python 3 and Python 2 is much greater, therefore
writing code that works in both Python 2 and Python 3 is a very complicated
process.

It is possible to `write code that works on Python 2.6, 2.7 and 3.3
<http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/>`_. This
ranges from tricky to extremely hard depending upon the kind of software
you are writing; if you're a beginner there are far more important things to
worry about.

Implementations
~~~~~~~~~~~~~~~

When people speak of *Python* they often mean not just the language but also
the CPython implementation. *Python* is actually a specification for a language
that can be implemented in many different ways.

CPython
-------

`CPython <http://www.python.org>`_ is the reference implementation of Python,
written in C. It compiles Python code to intermediate bytecode which is then
interpreted by a virtual machine. CPython provides the highest
level of compatibility with Python packages and C extension modules.

If you are writing open-source Python code and want to reach the widest possible
audience, targeting CPython is best. To use packages which rely on C extensions
to function, CPython is your only implementation option.

All versions of the Python language are implemented in C because CPython is the
reference implementation.

PyPy
----

`PyPy <http://pypy.org/>`_ is a Python interpreter implemented in a restricted
statically-typed subset of the Python language called RPython. The interpreter
features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).

PyPy aims for maximum compatibility with the reference CPython implementation
while improving performance.

If you are looking to increase performance of your Python code, it's
worth giving PyPy a try. On a suite of benchmarks, it's currently `over 5 times
faster than CPython <http://speed.pypy.org/>`_.

PyPy supports Python 2.7. PyPy3 [#pypy_ver]_, released in beta, targets Python 3.

Jython
------

`Jython <http://www.jython.org/>`_ is a Python implementation that compiles
Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine).
Additionally, it is able to import and use any Java class like a Python
module.

If you need to interface with an existing Java codebase or have other reasons to
need to write Python code for the JVM, Jython is the best choice.

Jython currently supports up to Python 2.5. [#jython_ver]_

IronPython
----------

`IronPython <http://ironpython.net/>`_  is an implementation of Python for the .NET
framework. It can use both Python and .NET framework libraries, and can also
expose Python code to other languages in the .NET framework.

`Python Tools for Visual Studio <http://ironpython.net/tools/>`_ integrates
IronPython directly into the Visual Studio development environment, making it
an ideal choice for Windows developers.

IronPython supports Python 2.7. [#iron_ver]_

.. [#pypy_ver] http://pypy.org/compat.html

.. [#jython_ver] http://wiki.python.org/jython/JythonFaq/GeneralInfo#Is_Jython_the_same_language_as_Python.3F

.. [#iron_ver] http://ironpython.codeplex.com/releases/view/81726
