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

When evaluating your need to use Python 2 over Python 3, it's worth noting that the 
final 2.x version 2.7 release came out in mid-2010, with a statement of extended 
support for this end-of-life release. 

There are some key issues that may require you to use Python 2 rather than Python 3:

- If you're deploying to an environment you don't control, that may impose a 
specific version, rather than allowing you a free selection from the available versions. 

- If you want to use a specific third party package or utility that doesn't yet have 
a released version that is compatible with Python 3, and porting that package is a 
non-trivial task, you may choose to use Python 2 in order to retain access to that package.


The Future (Python 3)
~~~~~~~~~~~~~~~~~~~~~

    Python 2.x is the status quo, Python 3.x is the shiny new thing.

`Further Reading <http://wiki.python.org/moin/Python2orPython3>`_

If you don't know which version to use, try Python 3.x. Some existing third-party 
software is not yet compatible with Python 3, and if you need to use such software, 
you can download Python 2.7.x instead.

Python 3, on the other hand, differs much more greatly from Python 2, so
writing code that works both on Python 2 and Python 3 is a very complicated
process.

It is still possible to `write code that works on Python 2.6, 2.7 and 3.3
<http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/>`_. Depending on
the kind of software you are writing, this might be either tricky or extremely
hard, and if you're a beginner there are much more important things to worry
about.

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
that rely on C extensions for their functionality (e.g., numpy) then CPython
is your only choice.

Being the reference implementation, all versions of the Python language are
available as CPython.

PyPy
----

`PyPy <http://pypy.org/>`_ is a Python interpreter implemented in a restricted
statically-typed subset of the Python language called RPython. The interpreter
features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).

PyPy aims for maximum compatibility with the reference CPython implementation
while improving performance.

If you are looking to squeeze more performance out of your Python code, it's
worth giving PyPy a try. On a suite of benchmarks, it's currently `over 5 times
faster than CPython <http://speed.pypy.org/>`_.

Currently PyPy supports Python 2.7. PyPy3 which targets Python 3 was recently
available as a beta release. [#pypy_ver]_

Jython
------

`Jython <http://www.jython.org/>`_ is a Python implementation that compiles
Python code to Java bytecode that is then executed in a JVM. It has the additional
advantage of being able to import and use any Java class like a Python
module.

If you need to interface with an existing Java codebase or have other reasons to
need to write Python code for the JVM, Jython is the best choice.

Jython currently supports up to Python 2.5. [#jython_ver]_

IronPython
----------

`IronPython <http://ironpython.net/>`_  is an implementation of Python for the .NET
framework. It can use both Python and .NET framework libraries, and can also
expose Python code to other .NET languages.

`Python Tools for Visual Studio <http://ironpython.net/tools/>`_ integrates
IronPython directly into the Visual Studio development environment, making it
an ideal choice for Windows developers.

IronPython supports Python 2.7. [#iron_ver]_

.. [#pypy_ver] http://pypy.org/compat.html

.. [#jython_ver] http://wiki.python.org/jython/JythonFaq/GeneralInfo#Is_Jython_the_same_language_as_Python.3F

.. [#iron_ver] http://ironpython.codeplex.com/releases/view/81726
