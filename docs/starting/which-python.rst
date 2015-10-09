Picking an Interpreter
======================

.. _which-python:

The State of Python (2 vs 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When choosing a Python interpreter, one looming question is always present:
"Should I choose Python 2 or Python 3"? The answer is not as obvious as
one might think.


The basic gist of the state of things is as follows:

1. Python 2.7 has been the standard for a *long* time.
2. Python 3 introduced major changes to the language, which many developers are unhappy with.
3. Python 2.7 will receive necessary security updates until 2020 [#pep373_eol]_.
4. Python 3 is continually evolving, like Python 2 did in years past.

So, you can now see why this is not such an easy decision.


Recommendations
~~~~~~~~~~~~~~~

I'll be blunt:


**Use Python 3 if...**

- You don't care.
- You love Python 3.
- You are indifferent towards 2 vs 3.
- You don't know which one to use.
- You embrace change.

**Use Python 2 if...**

- You love Python 2 and are saddened by the future being Python 3.
- The stability requirements of your software would be improved by a language and runtime that never changes.
- Software that you depend on requires it.


So.... 3?
~~~~~~~~~

If you're choosing a Python interpreter to use, and aren't opinionated, then I
recommend you use the newest Python 3.x, since every version brings new and
improved standard library modules, security and bug fixes. Progress is progress.

Given such, only use Python 2 if you have a strong reason to, such as a Python 2
exclusive library which has no adequate Python 3 ready alternative, or you
(like me) absolutely love and are inspired by Python 2.

Check out `Can I Use Python 3? <https://caniusepython3.com/>`_ to see if any
software you're depending on will block your adoption of Python 3.

`Further Reading <http://wiki.python.org/moin/Python2orPython3>`_

It is possible to `write code that works on Python 2.6, 2.7, and Python 3
<https://docs.python.org/3/howto/pyporting.html>`_. This
ranges from trivial to hard depending upon the kind of software
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

Jython currently supports up to Python 2.7. [#jython_ver]_

IronPython
----------

`IronPython <http://ironpython.net/>`_  is an implementation of Python for the .NET
framework. It can use both Python and .NET framework libraries, and can also
expose Python code to other languages in the .NET framework.

`Python Tools for Visual Studio <http://ironpython.net/tools/>`_ integrates
IronPython directly into the Visual Studio development environment, making it
an ideal choice for Windows developers.

IronPython supports Python 2.7. [#iron_ver]_

PythonNet
---------

`Python for .NET <http://pythonnet.github.io/>`_ is a package which
provides near seamless integration of a natively installed Python
installation with the .NET Common Language Runtime (CLR).  This is the
inverse approach to that taken by IronPython (see above), to which it
is more complementary than competing with.

In conjunction with Mono, PythonNet enables native Python
installations on non-Windows operating systems, such as OS X and
Linux, to operate within the .NET framework.  It can be run in
addition to IronPython without conflict.

PythonNet supports from Python 2.3 up to Python 2.7. [#pythonnet_ver]_

.. [#pypy_ver] http://pypy.org/compat.html

.. [#jython_ver] https://hg.python.org/jython/file/412a8f9445f7/NEWS

.. [#iron_ver] http://ironpython.codeplex.com/releases/view/81726

.. [#pythonnet_ver] http://pythonnet.github.io/readme.html

.. [#pep373_eol] https://www.python.org/dev/peps/pep-0373/#id2
